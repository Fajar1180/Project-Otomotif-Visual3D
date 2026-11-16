"""FastAPI application factory."""
import time
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.database import init_db
from app.routes.auth import router as auth_router
from app.routes.diagnosis import router as diagnosis_router

app = FastAPI(
    title="Otomotif AI API",
    description="Vehicle diagnostic and 3D configurator platform",
    version="0.1.0",
)

# Include routers
app.include_router(diagnosis_router)
app.include_router(auth_router)


# ---------------------------------------------------------------------------
# Global error envelope: {error, message, details?, request_id?}
# Success (2xx) responses are untouched.
# ---------------------------------------------------------------------------
_ERROR_CODES = {
    400: "VALIDATION_ERROR",
    401: "UNAUTHORIZED",
    403: "FORBIDDEN",
    404: "NOT_FOUND",
    409: "CONFLICT",
    422: "VALIDATION_ERROR",
    429: "RATE_LIMITED",
    500: "INTERNAL_ERROR",
}


def error_response(status_code: int, message: str, details=None, **extra) -> JSONResponse:
    """Build the API-spec error envelope."""
    payload = {"error": _ERROR_CODES.get(status_code, "ERROR"), "message": message}
    if details:
        payload["details"] = details
    payload.update(extra)
    return JSONResponse(status_code=status_code, content=payload)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    details = [
        {
            "field": ".".join(str(p) for p in err.get("loc", ()) if p != "body"),
            "message": err.get("msg", "Invalid value"),
        }
        for err in exc.errors()
    ]
    return error_response(422, "Invalid request payload", details)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return error_response(exc.status_code, str(exc.detail))


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    return error_response(500, "Terjadi error tak terduga", request_id=f"req-{uuid4()}")


# ---------------------------------------------------------------------------
# Rate limit: 100 req / 60s per IP, in-memory. Good enough for one process;
# swap for Redis when the API runs multi-worker.
# ---------------------------------------------------------------------------
_RATE_LIMIT = 100
_RATE_WINDOW = 60.0
_RATE_EXEMPT = ("/health", "/docs", "/redoc", "/openapi.json")
_hits: dict = {}


@app.middleware("http")
async def rate_limit(request: Request, call_next):
    path = request.url.path
    if path.startswith(_RATE_EXEMPT):
        return await call_next(request)

    ip = request.client.host if request.client else "unknown"
    now = time.monotonic()
    start, count = _hits.get(ip, (now, 0))
    if now - start >= _RATE_WINDOW:
        start, count = now, 0
    count += 1
    _hits[ip] = (start, count)

    if count > _RATE_LIMIT:
        retry_after = max(1, int(_RATE_WINDOW - (now - start)))
        response = error_response(
            429, "Terlalu banyak permintaan", retry_after=retry_after
        )
        response.headers["Retry-After"] = str(retry_after)
        return response

    response = await call_next(request)
    response.headers["X-RateLimit-Remaining"] = str(_RATE_LIMIT - count)
    return response


@app.on_event("startup")
async def startup():
    """Initialize database on startup."""
    init_db()


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
