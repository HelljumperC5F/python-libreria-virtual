from fastapi import FastAPI
from fastapi.responses import FileResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.libro import libro_router
from fastapi.middleware.cors import CORSMiddleware
from routers.categoria import categoria_router
from routers.user import user_router
from routers.http import http_router
import os

app = FastAPI()
app.title = "!!!"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(libro_router)
app.include_router(categoria_router)
app.include_router(user_router)
app.include_router(http_router)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/favicon.ico', tags=['home'])
def favicon():
    file_path = os.path.join(os.getcwd(), "html/favicon.ico")
    return FileResponse(file_path)


@app.get('/client-app', tags=['home'])
def client_app():
    file_path = os.path.join(os.getcwd(), "client-app.html")
    return FileResponse(file_path)


@app.get('/', tags=['home'])
def message():
    file_path = os.path.join(os.getcwd(), "html/index.html")
    return FileResponse(file_path)
