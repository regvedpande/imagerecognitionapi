# Image Recognition API

## Overview
This **Image Recognition API** leverages deep learning to identify and classify objects, scenes, and people in images. It uses **TensorFlow's MobileNetV2**, **OpenCV**, and **Flask** to provide a simple REST API that developers can integrate into their applications.

## Features
- Object, scene, and people recognition using **MobileNetV2**
- REST API for easy integration
- Image preprocessing with **OpenCV & Pillow**
- **Dockerized** for scalable deployment
- Hosted via **Flask** with **ngrok** support

## Tech Stack
- **Python 3.8+**
- **TensorFlow** (Deep Learning Model)
- **OpenCV & Pillow** (Image Processing)
- **Flask** (REST API Framework)
- **Docker** (Containerization)

## Installation & Setup
### Prerequisites
- Python 3.8+
- pip
- Docker (optional, for containerized deployment)

### Step 1: Clone the Repository
```sh
 git clone https://github.com/regvedpande/imagerecognitionapi.git
 cd imagerecognitionapi
```

### Step 2: Install Dependencies
```sh
 pip install -r requirements.txt
```

### Step 3: Run the Flask API
```sh
 python app.py
```

The API will be available at `http://127.0.0.1:5000` (or an ngrok URL in Colab).

## API Usage
### Endpoint: `/predict`
- **Method:** `POST`
- **Content-Type:** `multipart/form-data`
- **Parameter:** `file` (Image file in JPEG/PNG format)

### Example Request (cURL)
```sh
curl -X POST -F "file=@image.jpg" http://127.0.0.1:5000/predict
```

### Example Response
```json
{
  "predictions": [
    {"label": "n02124075", "description": "Egyptian cat", "probability": 0.95},
    {"label": "n02123045", "description": "Tabby cat", "probability": 0.03},
    {"label": "n02123159", "description": "Tiger cat", "probability": 0.02}
  ]
}
```

## Docker Deployment
### Build the Docker Image
```sh
 docker build -t image-recognition-api .
```

### Run the Container
```sh
 docker run -p 5000:5000 image-recognition-api
```

## Contribution
Feel free to open issues or submit pull requests.

## Contact
📧 **Email:** regregd@outlook.com

🔗 **GitHub Repo:** [Image Recognition API](https://github.com/regvedpande/imagerecognitionapi.git)

---
⭐ **If you find this project useful, please consider giving it a star on GitHub!** ⭐
