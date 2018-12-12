from pytesseract import *
import numpy as np
import cv2
import directory

pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

#option 1은 image_list 
#option 0은 폴더를 읽어 들임
def text_recognition(image_list,text,option=1):
    if option == 1:
        read_image_list(image_list,text)
    elif option == 0:
        filelist = directory.image_list('C:/Users/wnssp/Text-Recognition-master/Split')
        result = read_file(filelist)
        text.append(result)
    return text

def ocr(image,lang='eng'):
    #psm 옵션 6 : Assume a single uniform block of text
    #psm 옵션 7 : Treat the image as a single text line
    #옵션 6으로 해야 회사이름이 추출됨
    #SIGMA back의 경우 config option : --oem 1 --psm 3
    #DAEJUNG의 경우 config option : --oem 1 --psm 6
    processed_ocr = image_to_string(image,lang=lang,config='--oem 1 --psm 6')
    return processed_ocr

def read_image_list(image_list,text):
    for image in image_list:
        t = ocr(image)
        text.append(t)
    return text

def read_file(filelist):
    text = []
    for filename in filelist:
        ti = cv2.imread('Split/'+str(filename))
        t = ocr(ti)
        text.append(t)
    return text

if __name__ == '__main__':
    pass
else:
    print(str(__name__)+' module loaded')
    