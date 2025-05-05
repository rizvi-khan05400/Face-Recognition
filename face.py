# Face Recognition
# Importing OpenCV
import cv2

# Face Detection Model
# Note: ("C:/Users/Rizvi Khan/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml") where your pkage installed there yiu will get this line. In short your pkage location 
face_cap = cv2.CascadeClassifier("C:/Users/Rizvi Khan/AppData/Local/Programs/Python/Python313/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Initializing Video Capture
video_cap = cv2.VideoCapture(0)

# Main Loop
while True :


    ret , video_data = video_cap.read()

    # Converting Frame To Grayscale
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)

    # Face Detection
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Drawing The Rectangles Around Faces
    for (x, y, w, h) in faces:
        cv2.rectangle(video_data,(x, y),(x + w, y + h),(0, 255, 0),2)

    # Displaying The Video Frame
    cv2.imshow("live_camera",video_data)

    # Breaking Loop
    if cv2.waitKey(10) == ord("e"):
        break

# Releasing The Video Capture
video_cap.release()
