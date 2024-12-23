from fastapi import FastAPI, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Hi world!"}


@app.get("/hello/{name}")
async def hello(name: str = Path(..., min_length=1, max_length=20), page: int = Path(..., ge=1)):
    return {"message": f"Hello {name}!, page={page}"}
