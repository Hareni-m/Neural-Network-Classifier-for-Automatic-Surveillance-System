import cv2

# Function to preprocess the image
def preprocess_image(image):
    # Apply preprocessing techniques to enhance image quality
    # Example: Resize, contrast adjustment, noise reduction, etc.
    return image

# Load the cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load and preprocess known face images
known_face_1 = preprocess_image(cv2.imread('known_faces/hareni 2.jpg'))
known_face_2 = preprocess_image(cv2.imread('known_faces/hareni 3.jpg'))

# Function for face recognition
def recognize_face(img):
    # Detect faces
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5)
    
    # Preprocess the image before recognition
    img = preprocess_image(img)
    
    # Perform face recognition
    # Use preprocessed known_face_1 and known_face_2 for comparison
    
    # Display the output
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, "Face Found", (x, y-5), cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)
    cv2.imshow('Face Recognition', img)
    cv2.waitKey(1)  # Change wait time to 1 millisecond

# Main function
def main():
    # Capture video from webcam or load an image
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        recognize_face(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
