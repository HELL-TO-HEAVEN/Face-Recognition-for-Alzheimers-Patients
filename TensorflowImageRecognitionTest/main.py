import face_recognition

knownImage = face_recognition.load_image_file("./images/3.jpg")
knownImage1 = face_recognition.load_image_file("./images/2.jpg")
unknownImage = face_recognition.load_image_file("./HOWARD.jpg")

known_encoding = face_recognition.face_encodings(knownImage)[0]
known1_encoding = face_recognition.face_encodings(knownImage1)[0]
unknown_encoding = face_recognition.face_encodings(unknownImage)[0]

results = face_recognition.compare_faces([known_encoding, known1_encoding], unknown_encoding)

print(results)
