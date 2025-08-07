import cv2  # Import OpenCV

# Step 1: Connect to default camera (0 = laptop webcam)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Step 2: Loop to read and show frames
while True:
    ret, frame = cap.read()  # Read frame from camera

    if not ret:
        print("Camera not found or disconnected.")
        break

    # Step 3: Display the frame in a window
    cv2.imshow("Live CCTV", frame)

    # Step 4: Wait for 'q' key to exit or window close
    key = cv2.waitKey(1)
    if key == ord('q') or cv2.getWindowProperty("Live CCTV", cv2.WND_PROP_VISIBLE) < 1:
        print("Q pressed or window closed, exiting...")
        break
# ...existing code...