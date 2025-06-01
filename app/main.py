from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.v1 import router as v1_router

app = FastAPI(title="Fuse", debug=True)
app.include_router(v1_router, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        # Add Zap's dev and prod URLs here
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
