import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

# Load image
image_path = os.path.join('input', 'arial.png')  # or 'bev_sample.jpg'
if not os.path.exists(image_path):
    raise FileNotFoundError("Image not found!")

img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show original
plt.figure(figsize=(10, 6))
plt.imshow(img_rgb)
plt.title("Original BEV Image")
plt.axis('off')
plt.show()

# Run detection
# Run detection
print("Running YOLOv8...")
model = model = YOLO("yolov8n") 
print("✅ Model loaded!")
results = model(img_rgb, conf=0.1)  # Lower threshold to allow more guesses

boxes = results[0].boxes
print("Raw detection output:", boxes)

if boxes is not None and len(boxes) > 0:
    print(f"✅ Detected {len(boxes)} object(s).")
    annotated_img = results[0].plot()

    plt.figure(figsize=(10, 6))
    plt.imshow(annotated_img)
    plt.title("Detected Objects")
    plt.axis('off')
    plt.show()
else:
    print("❌ No objects detected. Try a street image or lower conf threshold.")


# Simulated metadata
sensor_data = {
    "vehicle_speed_kmph": np.random.randint(30, 80),
    "gps": {
        "lat": round(np.random.uniform(45.5, 45.51), 6),
        "lon": round(np.random.uniform(-73.57, -73.56), 6)
    },
    "weather": np.random.choice(["Clear", "Rainy", "Foggy"]),
    "timestamp": "2025-07-30 00:10:00"
}

print("\nSimulated Sensor Metadata:")
for k, v in sensor_data.items():
    print(f"{k}: {v}")
