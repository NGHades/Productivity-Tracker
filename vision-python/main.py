import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as drawing
import mediapipe.python.solutions.drawing_styles as drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands = 2,
    min_detection_confidence=0.5
)

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

    # Convert the frame from BGR to RGB (required by MediaPipe)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame for hand detection and tracking
    hands_detected = hands.process(frame)

    # Convert the frame from RGB to BGR (required by OpenCV)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)


    if hands_detected.multi_hand_landmarks:
        for hand_landmarks in hands_detected.multi_hand_landmarks:
            drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                drawing_styles.get_default_hand_landmarks_style(),
                drawing_styles.get_default_hand_connections_style(),
            )

    #Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(20) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows