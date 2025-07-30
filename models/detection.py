from ultralytics import YOLO

def run_object_detection(image_rgb, model_path="yolov8n", conf=0.1):
    model = YOLO(model_path)
    results = model(image_rgb, conf=conf)
    return results