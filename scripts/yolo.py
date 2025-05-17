import cv2
import torch
from ultralytics import YOLO

model = torch.hub.load('yolov8n')
cap = cv2.VideoCapture('scripts/video.mp4')

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    names = results.pandas().xyxy[0]['name']
    for name in names:
        print(name)
    
    results = model(frame)[0]  
    boxes = results.boxes
    names = results.names

    annotated_frame = results.plot()

    for box in boxes:
        class_id = int(box.cls[0])
        print(names[class_id])

    annotated_frame = results.plot()


    annotated_frame = results.render()[0]
    cv2.imshow('Webcam', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    

cap.release()
cv2.destroyAllWindows()
