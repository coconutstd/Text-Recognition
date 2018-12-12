import cv2
import numpy as np
import directory

class ImageProcessing: 

    def __init__(self,image,block_size,minus,kernel_size1,kernel_size2,ratio):
        self.image = image
        self.image_list = []
        self.block_size = block_size
        self.minus = minus
        #Morphological Transformations에 사용할 커널 크기
        #DAEJUNG의 Gradient 커널 크기는 2 x 2
        #DAEJUNG의 Closing 커널 크기는 5 x 3
        self.kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT,kernel_size1)
        self.kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,kernel_size2)
        self.ratio = ratio
        self.processing()
    
    def processing(self):
        self.gray()
        self.gradient()
        self.binarization()
        self.closing()
        self.find_contours()
        self.remove_files()
        self.__segmentation()
        
    def gradient(self):
        self.gradient_image = cv2.morphologyEx(self.gray_image,\
                                cv2.MORPH_GRADIENT, self.kernel1)
        return self.gradient_image
   
    def gray(self):
        self.gray_image = cv2.cvtColor(self.image,\
                                cv2.COLOR_BGR2GRAY)
        return self.gray_image
    
    def binarization(self):
        #block size는 3이 적절
        #차감값은 12 또는 7
        self.binary_image = cv2.adaptiveThreshold(self.gradient_image,\
                                255,\
                                cv2.ADAPTIVE_THRESH_MEAN_C,\
                                cv2.THRESH_BINARY_INV,\
                                self.block_size,\
                                self.minus)
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
        directory.remove_all_files('C:/Users/wnssp/Text-Recognition-master/Split')
    
    def show(self,name,obj):
        cv2.imshow(name,obj)
    
    def histogram_equal(self,image):
        clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(2,2))
        self.clahe_image = clahe.apply(image)
        return self.clahe_image
    
    def get_image_list(self):
        return self.image_list
        
    def __segmentation(self):
        idx = 0
        for c in self.contours:
            x,y,w,h = cv2.boundingRect(c)
            if w>50 and h>10:
                idx += 1
                new_img = self.image[y:y+h,x:x+w]
                large_new_img = cv2.resize(new_img,(0,0),fx=self.ratio,fy=self.ratio)
                self.image_list.append(large_new_img)
                cv2.imwrite('Split/'+str(idx)+'.jpg',large_new_img)

if __name__ == '__main__':
    pass
else:
    print(str(__name__)+' module loaded')