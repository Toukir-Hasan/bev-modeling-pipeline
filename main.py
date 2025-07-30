import os
import cv2
import matplotlib.pyplot as plt
from models.detection import run_object_detection
from models.lane_detection import detect_lanes
from utils.metadata_simulator import generate_sensor_metadata
from utils.formatter import format_output
from utils.grind_mapper import create_voxel_scene

# Load image
image_path = os.path.join('input', 'arial_2.jpg')
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show original
plt.imshow(img_rgb)
plt.title("Original BEV Image")
plt.axis('off')
plt.show()

# Run detection
results = run_object_detection(img_rgb)
boxes = results[0].boxes
annotated_img = results[0].plot()

plt.imshow(annotated_img)
plt.title("Detected Objects")
plt.axis('off')
plt.show()

# Run lane detection
lane_img, lanes = detect_lanes(img_rgb)

plt.imshow(lane_img)
plt.title("Detected Lanes")
plt.axis('off')
plt.show()

# Simulated metadata
sensor_data = generate_sensor_metadata()

print("\nSimulated Metadata:")
for k, v in sensor_data.items():
    print(f"{k}: {v}")


output = format_output(sensor_data, boxes, lanes)

# Optionally convert to JSON
import json
with open("output/scene_summary.json", "w") as f:
    json.dump(output, f, indent=2)

# Or preview in terminal
print(json.dumps(output, indent=2))

create_voxel_scene(output)