import math

import cv2
import numpy as np
import pytesseract
from PIL import Image

def contrast_and_brightness2(img) -> object:
    c = 100 / 255.0 
    k = math.tan((45 + 44 * c) / 180 * math.pi)

    img = (img - 127.5 ) * k + 127.5
    img = np.clip(img, 0, 255).astype(np.uint8)
    return img

def convert(id) -> str:
    try:
        Image.open(f'{id}')
    except:
        return ''
    img = cv2.imread(id)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = contrast_and_brightness2(gray)
    
    text = pytesseract.image_to_string(gray, lang="chi_tra")
    text = text if text else '無辨識到任何文字'

    return text