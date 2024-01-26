# Import libraries
import cv2
import numpy as np
import moviepy.editor as mp

# Load the video file
video = mp.VideoFileClip("IMG_4493.mov")

# Resize the video by 50%
video = video.resize(1.)

# Define the color range for the green background
# lower_green = np.array([100, 120, 60])
# upper_green = np.array([100, 255, 100])

lower_green = np.array([30, 50, 0])
upper_green = np.array([120, 255, 100])

# Define a function to apply chroma key
def chroma_key(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Create a mask for the green background
    mask = cv2.inRange(hsv, lower_green, upper_green)
    # Invert the mask to get the foreground
    mask_inv = cv2.bitwise_not(mask)
    # Apply the mask to the frame
    result = cv2.bitwise_and(frame, frame, mask=mask_inv)
    # Return the result
    return result

# Apply the chroma key function to each frame of the video
new_video = video.fl_image(chroma_key)

# Save the new video file
new_video.write_videofile("muppet1.mp4")