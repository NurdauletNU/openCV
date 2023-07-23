# 3.Попробовать реализовать обработчик видео, который через
# каждую секунду записывает все лица с видео в папку.

import cv2
import os
import time


def detect_faces(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces


def main():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    video_path = 'walking.mp4'
    output_folder = 'output_video'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_capture = cv2.VideoCapture(video_path)
    frame_rate = video_capture.get(cv2.CAP_PROP_FPS)
    interval = int(frame_rate)

    frame_count = 0
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_count += 1

        if frame_count % interval == 0:
            faces = detect_faces(frame, face_cascade)
            for i, (x, y, w, h) in enumerate(faces):
                face = frame[y:y + h, x:x + w]
                face_filename = f'face_{frame_count}_{i}.jpg'
                face_filepath = os.path.join(output_folder, face_filename)
                cv2.imwrite(face_filepath, face)

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
