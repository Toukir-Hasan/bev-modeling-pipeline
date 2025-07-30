import numpy as np

def generate_sensor_metadata():
    return {
        "vehicle_speed_kmph": np.random.randint(30, 80),
        "gps": {
            "lat": round(np.random.uniform(45.5, 45.51), 6),
            "lon": round(np.random.uniform(-73.57, -73.56), 6)
        },
        "weather": np.random.choice(["Clear", "Rainy", "Foggy"]),
        "timestamp": "2025-07-30 00:10:00"
    }
