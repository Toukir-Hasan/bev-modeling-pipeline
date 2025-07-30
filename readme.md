#  BEV Scene Modeling with Multimodal Inputs and 3D Reconstruction

This project simulates an end-to-end **Bird’s Eye View (BEV) perception pipeline** inspired by real-world autonomous driving systems. It integrates **object detection**, **lane line extraction**, **simulated sensor metadata**, and **3D voxel grid scene modeling**, providing a modular and extensible framework for autonomous perception.

---

##  Project Motivation
Autonomous vehicles perceive the world through multiple sensors. This project emulates that by combining:
- BEV-style top-down camera input
- YOLOv8 object detection
- Lane detection using OpenCV
- Simulated metadata like speed, GPS, weather
- 3D voxel scene visualization using matplotlib

This architecture reflects how real-world AV systems fuse multimodal data for perception and decision-making. Though the input data is limited, the project structure and modularization are designed to mirror production systems.

---

## 🔧 Tools Used
- **Python 3.9**
- **YOLOv8 (Ultralytics)** – Object detection
- **OpenCV** – Lane detection via Hough Transform
- **NumPy** – Data handling
- **Matplotlib (3D)** – Scene visualization
- **Streamlit** – Interactive frontend

---

##  Pipeline Components
```
[BEV Input Image]
       ↓
[YOLOv8 Object Detection]
       ↓
[OpenCV Lane Detection]
       ↓
[Simulated Sensor Metadata (Speed, GPS, Weather)]
       ↓
[3D Scene Modeling (Voxel Grid)]
       ↓
[Streamlit Dashboard (Frontend - Optional)]
```

---

## 🗂 Project Structure
```
bev_modeling/
├── data/                   # Input image
├── output/                 # scene_summary.json, 3D output
├── models/
│   ├── detection.py        # YOLO wrapper
│   └── lane_detection.py   # OpenCV Hough transform
├── utils/
│   ├── formatter.py        # Combine outputs
│   ├── metadata_simulator.py # Fake GPS/speed/weather
│   └── grid_mapper.py      # 3D voxel scene
├── main.py                 # Orchestrator
├── app.py                  # Streamlit frontend
└── requirements.txt
```

---

## 🖼 Output Example
- Red 3D boxes = Detected vehicles or objects
- Green lines = Lane segments on the road
- Label = GPS coordinates for spatial context

**Note:** Visual results may vary due to input quality and lighting conditions. The goal was to simulate the processing pipeline structure, not perfect detections.

---

##  How to Run It
1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the pipeline:
```bash
python main.py
```
4. Launch the frontend (optional):
```bash
streamlit run app.py
```

---

##  What Makes This Unique
- Simulates **multimodal sensor fusion** without requiring expensive LiDAR or GPS data
- Modular design mimics **real microservices** used in AV perception stacks
- Includes a 3D voxel grid scene — easy to demo or extend
- Designed with future extensions in mind (API, cloud, LiDAR, etc.)

---

##  Future Work
- Integrate real-time video input
- Add real LiDAR or stereo depth for richer 3D scenes
- Use FastAPI to expose each module as a REST microservice
- Deploy to cloud (Azure, HF Spaces) for public testing

---

