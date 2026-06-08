# backend

import cv2
import numpy as np
from keras.models import load_model

model = load_model('emotion_model.h5')
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

def detect_emotion(image_file):
    img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype('float32') / 255.0
        roi = np.expand_dims(roi, axis=0)
        prediction = model.predict(roi)[0]
        emotion = emotion_labels[np.argmax(prediction)]
        return emotion

    return "Neutral"

 
# Copyright © 2026 Osasere H. Ero. All rights reserved.
# Proprietary and confidential. Unauthorized copying of this file, via any medium, is strictly prohibited.
 
