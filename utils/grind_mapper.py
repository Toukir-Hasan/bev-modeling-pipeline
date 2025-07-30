import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def create_voxel_scene(scene_data):
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Plot detected objects as 3D bars
    for obj in scene_data["object_detections"]:
        x = (obj["x1"] + obj["x2"]) / 2
        y = (obj["y1"] + obj["y2"]) / 2
        z = 0
        dx, dy, dz = 15, 15, 10
        ax.bar3d(x, y, z, dx, dy, dz, color='red', alpha=0.6)

    # Plot lane lines as green 3D lines
    for line in scene_data["lane_lines"]:
        x_vals = [line["x1"], line["x2"]]
        y_vals = [line["y1"], line["y2"]]
        z_vals = [0, 0]  # on the road plane
        ax.plot(x_vals, y_vals, z_vals, color='green', linewidth=2)

    # Optional: Mark GPS location
    gps = scene_data.get("sensor_metadata", {}).get("gps", {})
    if gps:
        ax.text2D(0.05, 0.95, f"GPS: ({gps['lat']}, {gps['lon']})", transform=ax.transAxes)

    ax.set_title("3D Voxel Grid - BEV Scene")
    ax.set_xlabel("X (Image Pixel X)")
    ax.set_ylabel("Y (Image Pixel Y)")
    ax.set_zlabel("Z")
    ax.view_init(elev=30, azim=120)
    plt.tight_layout()
    plt.show()