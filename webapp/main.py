from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import models, schemas
from .database import SessionLocal, engine

"""Base.metadata.create_all() allows you to write just one class per table to use 
	- in the app
	- in the python outside the app
	- in db
"""
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


"""Dependency
* get_db() creates a new session for the next request.
"""
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Routes ...