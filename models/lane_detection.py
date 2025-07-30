import cv2
import numpy as np

def region_of_interest(img):
    height, width = img.shape[:2]
    mask = np.zeros_like(img)

    # Define a polygon (adjust as needed)
    polygon = np.array([[
        (int(0.1 * width), height),
        (int(0.45 * width), int(0.5 * height)),
        (int(0.55 * width), int(0.5 * height)),
        (int(0.9 * width), height)
    ]], np.int32)

    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def detect_lanes(image_rgb):
    img_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 70, 150)

    # Apply region mask
    masked_edges = region_of_interest(edges)

    lines = cv2.HoughLinesP(
        masked_edges,
        rho=1,
        theta=np.pi / 180,
        threshold=80,
        minLineLength=40,
        maxLineGap=25
    )

    lane_image = image_rgb.copy()
    line_coords = []

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            line_coords.append((x1, y1, x2, y2))
            cv2.line(lane_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return lane_image, line_coords

