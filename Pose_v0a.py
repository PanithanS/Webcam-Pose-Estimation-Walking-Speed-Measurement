from ultralytics import YOLO
import cv2
import math 

# start Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#image_size is 640 x 480
# model

#model = YOLO("yolo-Weights/yolov8s.pt")
model = YOLO('yolo-Weights/yolov8n-pose.pt')  # load a pretrained YOLOv8n pose model

results = model(source = 0, show=True, conf = 0.6)