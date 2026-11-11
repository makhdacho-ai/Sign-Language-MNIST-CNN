
import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

# 1. Déterminer le dossier principal du projet
PROJECT_DIR = Path(__file__).resolve().parents[2]

# 2. Charger le modèle CNN
MODEL_PATH = PROJECT_DIR / "models" / "sign_language_cnn.keras"
model = tf.keras.models.load_model(MODEL_PATH)

# 3. Correspondance des 24 classes
LETTERS = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y"
]

# 4. Ouvrir la webcam
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la caméra.")
    exit()

print("Webcam active ! Appuie sur Q pour quitter.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Erreur de lecture de la caméra.")
        break

    # 5. Définir une zone de prédiction
    height, width = frame.shape[:2]

    x1 = width // 2 - 150
    y1 = height // 2 - 150
    x2 = width // 2 + 150
    y2 = height // 2 + 150

    roi = frame[y1:y2, x1:x2]

    # 6. Prétraiter l'image
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28))
    normalized = resized.astype("float32") / 255.0
    input_image = normalized.reshape(1, 28, 28, 1)

    # 7. Prédiction CNN
    predictions = model.predict(input_image, verbose=0)

    predicted_index = int(np.argmax(predictions[0]))
    confidence = float(predictions[0][predicted_index]) * 100
    predicted_letter = LETTERS[predicted_index]

    # 8. Afficher la zone de détection
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # 9. Afficher la prédiction
    text = f"Lettre: {predicted_letter} ({confidence:.1f}%)"

    cv2.putText(
        frame,
        text,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Sign Language Recognition - CNN", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

