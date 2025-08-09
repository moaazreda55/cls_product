from fastapi import FastAPI, File, UploadFile, HTTPException
import io
import os
import numpy as np
from PIL import Image
from infer import classifier_google, classifier_facebook, classifier_resnet


app = FastAPI()


@app.post('/predict/google')
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    image.save("image.jpg")
    preds = classifier_google("image.jpg")
    return {"message":"Image uploaded successfully" ,"preds" : preds}


@app.post('/predict/resnet50')
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    image.save("image.jpg")
    preds = classifier_resnet("image.jpg")
    return {"message":"Image uploaded successfully" ,"preds" : preds}


@app.post('/predict/facebook')
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    image.save("image.jpg")
    preds = classifier_facebook("image.jpg")
    return {"message":"Image uploaded successfully" ,"preds" : preds}


