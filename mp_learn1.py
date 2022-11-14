import mediapipe as mp
from PIL import Image

img = Image.open('jame.jpeg')
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

result = mp_face_detection.FaceDetection()