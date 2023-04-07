import face_recognition
import cv2
import numpy as np
import cmake
import os

video_capture=cv2.VideoCapture(0)

#Loading known faces
user_inputs=input("Enter the folder path\n")
known_face_encodings=[]
known_face_names=[]
folder_path=user_inputs
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        filename_face=face_recognition.load_image_file(file_path)
        try:
            filename_encodings=face_recognition.face_encodings(filename_face)[0]
            known_face_encodings.append(filename_encodings)
            known_face_names.append(f"{filename}".replace(".jpg",""))
        except:
            continue
        


names=known_face_names.copy()

face_encodings=[]
face_locations=[]



while True:
    isTrue, frame=video_capture.read()
    small_frame=cv2.resize(frame, (0,0), fx=0.25, fy=0.25)
    rgb_small_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #recognising faces
    face_locations=face_recognition.face_locations(frame)
    face_encodings=face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        matches=face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distance=face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index=np.argmin(face_distance)

        if(matches[best_match_index]):
            name=known_face_names[best_match_index]
            if name in known_face_names:
                font=cv2.FONT_HERSHEY_SIMPLEX
                bottomLestCornerOfText=(10,100)
                fontScale=1.5
                fontColor=(255, 0, 0)
                thickness=3
                lineType=2
                cv2.putText(frame, name, bottomLestCornerOfText, font, fontScale, fontColor, thickness, lineType)
            else:
                cv2.putText(frame, "No match")
        cv2.imshow("frame",frame)
        if(cv2.waitKey(20) & 0xFF==ord("q")):
            break

video_capture.release()
cv2.destroyAllWindows()

