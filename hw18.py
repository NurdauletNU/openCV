# 2.Найти возможность поиска лиц(а) на фото, и его вырезку

import cv2
import os


def detect_faces(image_path, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) == 0:
        print("Лица не обнаружены на данной фотографии.")
        return

    for i, (x, y, w, h) in enumerate(faces):
        face = image[y:y + h, x:x + w]
        face_filename = f'face_{os.path.basename(image_path)}_{i}.jpg'
        face_filepath = os.path.join(output_folder, face_filename)
        cv2.imwrite(face_filepath, face)

    print(f"Обнаружено {len(faces)} лиц(о) на фотографии.")


def main():
    image_path = 'collegues.jpg'
    output_folder = 'output_photo'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if image_path:
        detect_faces(image_path, output_folder)


if __name__ == "__main__":
    main()
