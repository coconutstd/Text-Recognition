import numpy as np
import cv2

def process(img):
    
    imgray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    w, h = imgray.shape[:2]

    templ = cv2.imread("Images/want.jpg", cv2.IMREAD_GRAYSCALE)
    templ_h, templ_w = templ.shape[:2]
    res = cv2.matchTemplate(imgray, templ, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.34)
    print(np.shape(loc))
    if(np.size(loc[1]>=2)):
        return True
    else:
        return False

