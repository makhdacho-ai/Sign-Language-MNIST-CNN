import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Erreur : caméra inaccessible")
    exit()

print("Caméra ouverte !")
print("Initialisation...")

time.sleep(2)

for i in range(20):
    ret, frame = cap.read()

    if ret:
        print("Image reçue :", frame.shape)

        frame = cv2.resize(frame, (960, 540))
        cv2.imshow("Ma webcam", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print(f"Lecture impossible : tentative {i+1}")

    time.sleep(0.2)

cap.release()
cv2.destroyAllWindows()

print("Test terminé.")