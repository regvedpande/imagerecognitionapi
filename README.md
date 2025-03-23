# Image Recognition API
A REST API for identifying objects in images using MobileNet-SSD (Caffe).

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run the API: `python app.py`
3. Test with: `curl -X POST -F "image=@test.jpg" http://localhost:5000/recognize`

## Docker
- Build: `docker build -t image-recognition-api .`
- Run: `docker run -p 5000:5000 image-recognition-api`