import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(1)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')

filename = sys.argv[1] + ".avi"

out = cv2.VideoWriter(filename,fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == 27:
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
