from pytesseract import *
import numpy as np
import cv2
import directory

pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

class OcrProcessing:
    def __init__(self):
        self.text = []
    
    def processing(self):
        filelist = directory.image_list('C:/Users/wnssp/캡스톤프로젝트4/Split')
        self.__read_file(filelist)
        return self.text
        
    def ocr(self,image,lang='eng'):
        #psm 옵션 6 : Assume a single uniform block of text
        #psm 옵션 7 : Treat the image as a single text line
        #옵션 6으로 해야 회사이름이 추출됨
        processed_ocr = image_to_string(image,lang=lang,config='--oem 1 --psm 6')
        return processed_ocr
    
    def __read_file(self,filelist):
        for filename in filelist:
            ti = cv2.imread('Split/'+str(filename))
            t = self.ocr(ti)
            self.text.append(t)

if __name__ == '__main__':
    pass
else:
    print(__name__)
    