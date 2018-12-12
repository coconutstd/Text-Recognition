import cv2
import re
import image_process
import ocr_process as ocr
import regex_process
import knnTest

def sigma(iter):
    front_image = cv2.imread('Images/SIGMA_front_crop'+str(iter)+'.jpg')
    back_image = cv2.imread('Images/SIGMA_back_crop'+str(iter)+'.jpg')
    process1 = image_process.ImageProcessing(front_image,3,6,(2,2),(3,2),1.5)
    img_list = process1.get_image_list()
    process2 = image_process.ImageProcessing(back_image,3,10,(2,2),(3,2),1.5)
    img_list2 = process2.get_image_list()
    text = []
    ocr_text1 = ocr.text_recognition(img_list,text,1)
    ocr_text2 = ocr.text_recognition(img_list2,ocr_text1,1)
    regex = regex_process.RegexProcessing(ocr_text2)
    #print(regex.info)
    knnTest.searchFromDB(regex.info['product_code'],regex.info['product_name'],regex.info['cas_number'])

if __name__ == '__main__':
    pass
else:
    print(str(__name__)+' 테스트입니다')