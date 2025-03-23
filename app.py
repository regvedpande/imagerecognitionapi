import cv2 # type: ignore
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

MODEL_PATH = "model/mobilenet_iter_73000.caffemodel"
CONFIG_PATH = "model/deploy.prototxt"
LABELS_PATH = "utils/labels.txt"

with open(LABELS_PATH, "r") as f:
    LABELS = [line.strip() for line in f.readlines()]

net = cv2.dnn.readNetFromCaffe(CONFIG_PATH, MODEL_PATH)

def process_image(image_data):
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    blob = cv2.dnn.blobFromImage(img, 1.0/127.5, (300, 300), (127.5, 127.5, 127.5), swapRB=True)
    net.setInput(blob)
    detections = net.forward()
    results = []
    h, w = img.shape[:2]
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            class_id = int(detections[0, 0, i, 1])
            if class_id < len(LABELS):
                label = LABELS[class_id]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x, y, x2, y2) = box.astype("int")
                # Convert NumPy int32 to Python int
                x, y, x2, y2 = int(x), int(y), int(x2), int(y2)
                results.append({
                    "label": label,
                    "confidence": float(confidence),
                    "box": {
                        "x": x,
                        "y": y,
                        "width": x2 - x,
                        "height": y2 - y
                    }
                })
    return results

@app.route("/recognize", methods=["POST"])
def recognize():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400
    image_file = request.files["image"].read()
    try:
        results = process_image(image_file)
        return jsonify({"detections": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Image Recognition API - POST an image to /recognize"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)