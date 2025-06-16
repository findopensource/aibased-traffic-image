from ultralytics import YOLO
import cv2

def detect_vehicles(image_path, output_path):
    model = YOLO("yolov8n.pt")  # use the smallest model for speed
    results = model(image_path)
    annotated_frame = results[0].plot()
    cv2.imwrite(output_path, annotated_frame)
