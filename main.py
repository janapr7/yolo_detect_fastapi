from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from utils import detect_objects
from typing import List
import io

app = FastAPI()

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    annotated_img_bytes, boxes_info = detect_objects(image_bytes)

    return {
        "boxes": boxes_info
    }

@app.post("/detect/image")
async def detect_with_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    annotated_img_bytes, boxes_info = detect_objects(image_bytes)

    return StreamingResponse(io.BytesIO(annotated_img_bytes), media_type="image/jpeg")
