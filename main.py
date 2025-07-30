import os
import cv2
import matplotlib.pyplot as plt
from models.detection import run_object_detection
from models.lane_detection import detect_lanes
from utils.metadata_simulator import generate_sensor_metadata
from utils.formatter import format_output
from utils.grind_mapper import create_voxel_scene
import streamlit as st
import json
from PIL import Image

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



st.set_page_config(page_title="BEV Scene Visualizer", layout="wide")
st.title("🚗 BEV Modeling Demo")

# Upload image (just for display)
uploaded_file = st.file_uploader("Upload a BEV-style image (optional)", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

st.markdown("### 📂 Load Output File")

# Load your previously saved output
if st.button("Load and Visualize scene_summary.json"):
    try:
        with open("output/scene_summary.json", "r") as f:
            scene_data = json.load(f)

        st.subheader("📍 Sensor Metadata")
        st.json(scene_data["sensor_metadata"])

        st.subheader("📦 Detected Objects")
        st.write(f"Detected {len(scene_data['object_detections'])} objects")

        st.subheader("🛣️ Detected Lane Lines")
        st.write(f"Detected {len(scene_data['lane_lines'])} lane segments")

        st.subheader("🧱 3D Scene View")
        create_voxel_scene(scene_data)

    except FileNotFoundError:
        st.error("scene_summary.json not found. Please run the pipeline first.")