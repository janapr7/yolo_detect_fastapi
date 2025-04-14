Run FastAPI

1. Create virtual environment (recommended)
   python -m venv or python3 -m venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate # Windows

2. Install dependencies
   pip install -r requirements.txt

3. Run FastAPI
   uvicorn main:app --reload

Note:
Using YOLOv8l model

Test API example in local:
_To get detection result as image with bounding box_
curl -X POST http://localhost:8000/detect/image \
 -F "file=@/Users/jana/Documents/Research/Data/nov2024/dataset_v3/images/train/air_mars_byk_st_merq_tsat_b_008.jpg" --output output.jpg

_To get detection result data_
curl -X POST http://localhost:8000/detect \
 -F "file=@/Users/jana/Documents/Research/Data/nov2024/dataset_v3/images/train/air_mars_byk_st_merq_tsat_b_008.jpg"
