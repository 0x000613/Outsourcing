import cv2
import os

fps = 30

image_folder = os.path.realpath(os.path.dirname(__file__))
video_name = os.path.join(image_folder, 'video.mp4')

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, -1, fps, (width,height))

for image in images:
       video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()