import  face_recognition as fr
import os
import pickle

db_path = r'C:\Users\LENOVO\Documents\path\face_db'

faces = os.listdir(db_path)

known_face_encodings = []
n = 1

for face in faces:
#    if face.endswith('jpg'):
    im = fr.load_image_file(db_path  + face)
        
    encoding = fr.face_encodings(im)[0]
    known_face_encodings.append(encoding)
    print("%1d of %2d is done" %(n, len(faces)))
    n += 1

file = open(path+ 'encode.pickle', 'wb')
pickle.dump(known_face_encodings, file)
file.close()


