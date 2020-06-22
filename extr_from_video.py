import cv2
import os
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"                  # act as environment variable for pytesseract. 

cam = cv2.VideoCapture("vid.mp4")              # location of video.

try:

    # creating a folder name vid_frames
    if not os.path.exists('vid_frames'):
        os.makedirs('vid_frames')

    # if not created then raise error
except OSError:
    print('Error: Creating directory of data')


i=0

#counter for reducing frames
counter = 0

# 10 is ideal no. for this situation bcoz if we reduce or increase value the no. of frames will increase.
frame_skip=10

txt=''
txt1=''
while cam.isOpened():

    # reading from frame
    ret, frame = cam.read()

    if not ret:
        break
    if counter > frame_skip - 1:
        # if video is still left continue creating images
        name = './vid_frames/frame' + str(i) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)
        img = Image.open(name)

        txt1=pytesseract.image_to_string(img)
        if txt1 not in txt:
            txt=txt+" \n "+txt1
        else:
            pass
	# increamenting counter so that it show how many frames are created.
        i+=1       

        counter=0
        continue
        
	
    counter += 1

print("text : ",txt)

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
