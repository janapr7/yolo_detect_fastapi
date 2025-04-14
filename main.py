from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from utils import detect_objects
from typing import List
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
