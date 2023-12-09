from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from illusion import getRandomIllusion
import uuid

class Check(BaseModel):
    token: str
    answer: int

db = {}

app = FastAPI()
app.mount("/static", StaticFiles(directory="api/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/init")
def init(size: int):
    illusion = getRandomIllusion((size, size))
    token = str(uuid.uuid4())
    db[token] = illusion
    return {"token": token, "question": illusion.question, "len": illusion.n}

@app.get("/image/{idx}")
def get_image(idx: int, token: str):
    image = db[token].get_image(idx).tobytes()
    return Response(content=image, media_type="image/png")

@app.post("/check")
def check_answer(check: Check):
    if not db[check.token].check_answer(check.answer):
        db.pop(check.token)
        return {"status": False}
    return {"status": True}

@app.get("/check")
def check_passed(token: str):
    if token in db:
        db.pop(token)
        return {"status": True}
    return {"status": False}
