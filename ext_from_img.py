#extracting text from image.

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

a=input("enter image location with type : ")
b=input("enter text file name with location you want to create : ")
img=Image.open(a)
txt=pytesseract.image_to_string(img)
print(txt)

with open(b,"w") as f:
    f.write(txt)
