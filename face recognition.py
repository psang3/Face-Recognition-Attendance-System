# pip install cmake
# pip install face_recognition
# pip install opencv-python

import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import cmake


video_capture = cv2.VideoCapture(0)

# load known faces
face_image1 = face_recognition.load_image_file("image1.jpeg")
image1_encodings = face_recognition.face_encodings(face_image1)[0]
face_image2 = face_recognition.load_image_file("image2.jpeg")
image2_encodings = face_recognition.face_encodings(face_image2)[0]

known_face_encodings = [image1_encodings,image2_encodings]

known_face_names = ["Harry","Rohan"]

# list of expected students
students = known_face_names.copy()

face_location = []
face_encodings = []

# get current time

now = datetime.now()
current_data = now.strftime("%y-%m-%d")

f = open(f"{current_date}.csv", "w+", newline=" ")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    #recognize faces
    face_location = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_location)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance = face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argumin(face_distance)

        if(matches[best_match_index]):
            name = known_face_names[best_match_index]
        

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & OxFF == ord("q"):
            break









