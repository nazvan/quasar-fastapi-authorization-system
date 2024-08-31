from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

# from app.exceptions import TokenNotFoundException
from app.users.router import router as router_users
from app.images.router import router as router_images

app = FastAPI()

# Добавляем middleware для CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9005"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


app.include_router(router_users)
app.include_router(router_images)