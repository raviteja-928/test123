import cv2

# Load the cascadeclassifier for the face detection
face_cascade = cv2.CascadeClassifier('path_to_xml_file')

# Load the image
img = cv2.imread('path_to_image')

# Convert the image to gray scale 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 5)

# Draw rectangles around the faces
for (x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image
cv2.imshow('Faces', img)
cv2. waitkey(0)
cv2.destroyAllWindows()