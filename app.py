import sys
import os

import certifi
ca=certifi.where()

from dotenv import load_dotenv
load_dotenv()
mogo_db_url=os.getenv("MONGO_DB_URL")
print(mogo_db_url)
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import FileResponse
import pandas as pd

client=pymongo.MongoClient(mogo_db_url,tlsCAFile=ca)

from networksecurity.constant.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME

database=client[DATA_INGESTION_DATABASE_NAME]
collection=database[DATA_INGESTION_COLLECTION_NAME]

app=FastAPI()
origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.post("/train")
async def train_route():
    try:
        training_pipeline=TrainingPipeline()
        training_pipeline.run_pipeline()
        return Response(content="Training successful!!",media_type="text/plain")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
if __name__=="__main__":
    app_run(app,host="0.0.0.0",port=8000)