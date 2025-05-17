import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  

cap = cv2.VideoCapture('scripts/video.mp4')

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]  
    boxes = results.boxes
    names = results.names

    annotated_frame = results.plot()

    for box in boxes:
        class_id = int(box.cls[0])
        print(names[class_id])

    cv2.imshow('YOLOv8 Webcam', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
