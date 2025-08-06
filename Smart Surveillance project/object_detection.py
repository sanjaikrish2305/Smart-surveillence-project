from ultralytics import YOLO
import cv2

# Step 1: Load pre-trained YOLOv8 model (nano version – small and fast)
model = YOLO("yolov8n.pt")  # Pre-trained on 80 classes (COCO dataset)

# Step 2: Start video capture
cap = cv2.VideoCapture(0)  # 0 = default webcam

# Step 3: Continuous loop to detect objects in each frame
while True:
    ret, frame = cap.read()  # Read a frame from camera

    if not ret:
        print("Camera not working!")
        break

    # Step 4: Predict objects in the current frame using YOLOv8
    results = model.predict(frame, imgsz=640)

    # Step 5: Annotate the frame with boxes and labels
    annotated_frame = results[0].plot()

    # Step 6: Show the result
    cv2.imshow("Detection", annotated_frame)

    # Step 7: Break loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 8: Release camera and close all windows
cap.release()
cv2.destroyAllWindows()

