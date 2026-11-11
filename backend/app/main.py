"""FastAPI application factory."""
from fastapi import FastAPI
from app.database import init_db
from app.routes.diagnosis import router as diagnosis_router

app = FastAPI(
    title="Otomotif AI API",
    description="Vehicle diagnostic and 3D configurator platform",
    version="0.1.0",
)

# Include routers
app.include_router(diagnosis_router)


@app.on_event("startup")
async def startup():
    """Initialize database on startup."""
    init_db()


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}
