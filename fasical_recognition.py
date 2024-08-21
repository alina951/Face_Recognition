import cv2
import os
import face_recognition

## load known face encodings and names

known_face_encoding = []
known_face_names = []

## load known faces and their names here

known_person1_image = face_recognition.load_image_file(r"C:\Users\44784\OneDrive\Desktop\facial recognition\2pac.jpg")


known_face_encoding.append(face_recognition.face_encodings(known_person1_image)[0])


known_face_names.append("2pac")


#initalise webcam
video_capture = cv2.VideoCapture(0)
while True:
    # capture frame-by-frame
    ret, frame = video_capture.read()
    # fiad all face locations in the current frame 
    face_locations = face_recognition.face_locations(frame)

    #loop through each face found in the frame 
    for top, right, bottom, left in face_locations:
        #check if the face matches any known faces
        face_encoding = face_recognition.face_encodings(frame, [(top, right, bottom, left)])[0]
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        name = "unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # draw a box around teh face and label with the name
        cv2.rectangle(frame, (left,top),(right, bottom), (0,0,255), 2)
        cv2.putText(frame,name, (left,top -10),cv2.FONT_HERSHEY_SIMPLEX,0.9, (0,0,255), 2)

        #DISPLAY THE RESULTING FRAME
        cv2.imshow("video", frame)

        # break the loop when the 'q' key is pressed
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break

# relese the webcame and close open cc window 
video_capture.release()
cv2.destroyAllWindows()
