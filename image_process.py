import cv2
import numpy as np
import directory

class ImageProcessing: 
    #Morphological Transformations에 사용할 커널 크기
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,3))  
    
    def __init__(self,image):
        self.image = image
        self.processing()
    
    def processing(self):
        self.gradient()
        self.gray()
        self.binarization()
        self.closing()
        self.find_contours()
        self.remove_files()
        self.__segmentation()
        
    def gradient(self):
        self.gradient_image = cv2.morphologyEx(self.image,\
                                cv2.MORPH_GRADIENT, self.kernel1)
        return self.gradient_image
   
    def gray(self):
        self.gray_image = cv2.cvtColor(self.gradient_image,\
                                cv2.COLOR_BGR2GRAY)
        return self.gray_image
    
    def binarization(self):
        #block size는 3이 적절
        #차감값은 12 또는 7
        self.binary_image = cv2.adaptiveThreshold(self.gray_image,\
                                255,\
                                cv2.ADAPTIVE_THRESH_MEAN_C,\
                                cv2.THRESH_BINARY_INV,\
                                3,\
                                12)
        return self.binary_image
    
    def closing(self):
        self.close_image = cv2.morphologyEx(self.binary_image,\
                                cv2.MORPH_CLOSE, self.kernel2)
        return self.close_image
    
    def find_contours(self):
        self.contour_image, self.contours, hierachy = cv2.findContours(\
                                self.close_image,\
                                cv2.RETR_EXTERNAL,\
                                cv2.CHAIN_APPROX_SIMPLE)
        return self.contours
    
    def draw_contours(self):
        self.draw_image = cv2.drawContours(self.image,self.contours,-1,(0,255,0),3)
        return self.draw_image
    
    def remove_files(self):
        directory.remove_all_files('C:/Users/wnssp/캡스톤프로젝트4/Split')
        
    def __segmentation(self):
        idx = 0
        for c in self.contours:
            x,y,w,h = cv2.boundingRect(c)
            if w>50 and h>10 and h<70:
                idx += 1
                new_img = self.image[y:y+h,x:x+w]
                cv2.imwrite('Split/'+str(idx)+'.jpg',new_img)

if __name__ == '__main__':
    pass
else:
    print(__name__)