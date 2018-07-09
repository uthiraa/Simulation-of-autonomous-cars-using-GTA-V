# -*- coding: utf-8 -*-
# ROI

import numpy as np
from PIL import ImageGrab
import cv2
from directkeys import ReleaseKey, PressKey, W, A, S, D
import time
import pyautogui

def roi(img,vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=150, threshold2=250)
    vertices = np.array([[10,500], [10,900], [100,300],[1000,300],[1500,500],[1500,900]])
    processed_img = roi(processed_img, [vertices])
    return processed_img

def main():
    
    while(True):
        screen = np.array(ImageGrab.grab (bbox= (0, 40, 1500, 900)))
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()

