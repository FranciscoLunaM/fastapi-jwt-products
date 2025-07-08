from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session,select

from db import get_session
from models import *

app=FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

@app.get("/")
async def test():
    
    return {"message":"OK"}

@app.get("/test")
async def testDatabase(session: Session=Depends(get_session))->Test_table:
    test=session.exec(select(Test_table)).first()
    return test

#For production use: fastapi run