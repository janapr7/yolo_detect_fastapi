from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io

model = YOLO("model/model_v2.pt")

def detect_objects(image_bytes: bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    results = model(image)

    pred = results[0]

    annotated_img = pred.plot()
    _, img_encoded = cv2.imencode(".jpg", annotated_img)
    annotated_img_bytes = img_encoded.tobytes()

    boxes_info = []
    for box in pred.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        conf = float(box.conf[0])
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        boxes_info.append({
            "label": label,
            "confidence": conf,
            "bbox": [x1, y1, x2, y2]
        })

    speed = pred.speed
    timing = {
        "preprocess_ms": round(speed.get("preprocess", 0.0), 2),
        "inference_ms": round(speed.get("inference", 0.0), 2),
        "postprocess_ms": round(speed.get("postprocess", 0.0), 2),
    }
    timing["total_ms"] = round(sum(timing.values()), 2)

    return annotated_img_bytes, boxes_info, timing
