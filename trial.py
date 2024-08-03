# this is a trial script to capture video using webcam!

import cv2

# Open the default camera (usually the built-in camera on a Mac)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was not captured correctly, break the loop
    if not ret:
        print("Failed to grab frame")
        break

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()