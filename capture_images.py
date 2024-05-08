import cv2
import os

# Create a directory to store the images
output_dir = "known_faces"
os.makedirs(output_dir, exist_ok=True)

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

# Counter for naming the images
image_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Display the captured frame
    cv2.imshow('Capture Images - Press SPACE to save, ESC to exit', frame)

    # Check for key press events
    key = cv2.waitKey(1)

    # Check if SPACE key is pressed to capture and save the image
    if key == ord(' '):
        # Increment the image count
        image_count += 1

        # Define the file path for the captured image
        image_path = os.path.join(output_dir, f"face_{image_count}.jpg")

        # Save the captured image
        cv2.imwrite(image_path, frame)
        print(f"Image saved: {image_path}")

    # Check if ESC key is pressed to exit the program
    elif key == 27:  # ESC key
        break

# Release the video capture object and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
