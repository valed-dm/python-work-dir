import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routes.api import router as api_router
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

app = FastAPI(title="Menus API")

origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000,
                log_level="info", reload=True)
    print("running")
