import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: could not access webcam")
else:
    print("Webcam accessed successfully")

ret, frame = cap.read()

if ret:
    cv2.imshow("Captured Frame", frame)
    cv2.waitKey(0) # Wait for a key press to close the window
    cv2.destroyAllWindows()
else:
    print("Could not capture any frames")

cap.release()