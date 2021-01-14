import cv2
import os
import numpy as np

BASEDIR = os.path.realpath(os.path.dirname(__file__))

# Create a VideoCapture object
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter(os.path.join(BASEDIR, "output.avi"),cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
while(True):
  ret, frame = cap.read()
 
  if ret == True: 
     
    # Write the frame into the file 'output.avi'
    out.write(frame)
 
    # Display the resulting frame    
    cv2.imshow('frame',frame)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cap = cv2.VideoCapture(0)

print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter(os.path.join(BASE_DIR, "output.avi"), fourcc, 25.0, (640, 480))

while(True):
    ret, frame = cap.read()    # Read 결과와 frame
    if(ret) :
        gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)    # 입력 받은 화면 Gray로 변환
        cv2.imshow('frame_color', frame)    # 컬러 화면 출력        cv2.imshow('frame_gray', gray)    # Gray 화면 출력
        out.write(frame)

        if cv2.waitKey(1) == ord('q'):
            breakcap.release()
cv2.destroyAllWindows()