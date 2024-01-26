import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture('IMG_4492.mov')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 25.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define range of green color in HSV
        lower_green = np.array([20, 70, 70])
        upper_green = np.array([80, 255, 255])

        # Threshold the HSV image to get only green colors
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Invert the mask
        mask_inv = cv2.bitwise_not(mask)

        # Separate the foreground and background
        fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
        bg = cv2.bitwise_and(frame, frame, mask=mask)

        # Replace the green background with a transparent one
        bg[np.where((bg == [0, 255, 0]).all(axis=2))] = [0, 0, 0]

        # Merge the foreground and background
        final = cv2.add(fg, bg)

        # Write the output frame
        out.write(final)

        # Display the resulting frame
        cv2.imshow('frame', final)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
