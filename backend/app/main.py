"""FastAPI application factory."""
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


@app.on_event("startup")
async def startup():
    """Initialize database on startup."""
    init_db()


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
