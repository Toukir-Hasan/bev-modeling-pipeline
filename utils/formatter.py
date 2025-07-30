def format_output(sensor_data, boxes, lanes):
    detected_objects = []
    if boxes is not None:
        for box in boxes.xyxy.cpu().numpy():
            x1, y1, x2, y2 = box[:4]
            cls = int(box[5]) if len(box) > 5 else -1
            detected_objects.append({
                "class_id": int(cls),
                "x1": int(x1), "y1": int(y1),
                "x2": int(x2), "y2": int(y2)
            })

    return {
        "sensor_metadata": sensor_data,
        "object_detections": detected_objects,
        "lane_lines": [
            {
                "x1": int(x1), "y1": int(y1),
                "x2": int(x2), "y2": int(y2)
            }
            for (x1, y1, x2, y2) in lanes
        ]
    }
