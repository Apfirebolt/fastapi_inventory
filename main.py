from pathlib import Path
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from inventory.router import router as inventory_router

app = FastAPI(
    title="FastAPI Inventory API",
    docs_url="/docs",
    openapi_url="/openapi.json",
    version="0.0.1",
)

# Allow local dev servers (Vite default or custom 8080)
origins = [
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes - prefix with /api to avoid conflicts with frontend routes
app.include_router(inventory_router, prefix="/api/inventory", tags=["Inventory Items"])

@app.get("/api/health")
async def health_check():
    return {"message": "FastAPI Inventory API in FastAPI"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)