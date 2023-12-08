from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

CAPTCHA_SERVER = "http://localhost:8001"

app = FastAPI()
templates = Jinja2Templates(directory="example/templates")

@app.middleware("http")
def middleware(request: Request, call_next):
    return call_next(request)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", 
                                      {"request": request})

@app.get("/protected")
def protected(request: Request, token: str = None):
    if token and requests.get(f"{CAPTCHA_SERVER}/check", params={"token": token}).json()["status"]:
        return templates.TemplateResponse("protected.html",
                                          {"request": request})
    else:
        return templates.TemplateResponse("forbidden.html",
                                          {"request": request})