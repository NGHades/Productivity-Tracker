import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: could not access webcam")
    exit()
else:
    print("Webcam accessed successfully")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot receive input from video")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Display the resulting frame
    cv2.imshow("frame", gray)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows