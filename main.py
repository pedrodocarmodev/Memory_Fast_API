from fastapi import FastAPI, APIRouter
from core.database import Base, engine
from routers import training_router
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app = FastAPI(title="Memory API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], # restringir origens em produção
)

app.include_router(router=training_router.router)

Base.metadata.create_all(bind=engine)