import os
import cv2

# Directory where the dataset will be stored
DATA_DIR = 'data'

# Create the directory if it does not exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)


number_of_classes = 26

# Number of images to collect per class
dataset_size = 100


cap = cv2.VideoCapture(0)

# Loop through each class
for j in range(number_of_classes):
    # Create a directory for the current class if it does not exist
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Display a message on the frame to indicate readiness
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)

        # Show the frame in a window titled 'frame'
        cv2.imshow('frame', frame)

        # Wait for 25 milliseconds and check if 'Q' key is pressed
        # If 'Q' is pressed, exit the loop
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    # Collect dataset_size images for the current class
    while counter < dataset_size:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Display the frame in the window titled 'frame'
        cv2.imshow('frame', frame)

        # Wait for 25 milliseconds
        cv2.waitKey(25)

        # Save the frame as an image file in the corresponding class directory
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        # Increment the counter
        counter += 1

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
