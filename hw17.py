# 1.Добавить функционал программе по обработке фото

import cv2
import os


def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces


def process_image(image_path, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image = cv2.imread(image_path)
    faces = detect_faces(image, face_cascade)

    for i, (x, y, w, h) in enumerate(faces):
        face = image[y:y + h, x:x + w]
        face_filename = f'face_{os.path.basename(image_path)}_{i}.jpg'
        face_filepath = os.path.join(output_folder, face_filename)
        cv2.imwrite(face_filepath, face)

    return image


def main():
    image_path = 'src.jpg'
    output_folder = 'output_photo'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if image_path:
        processed_image = process_image(image_path, output_folder)
        cv2.imshow('Processed Image', processed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
