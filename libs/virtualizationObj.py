import pyautogui
import cv2
import numpy as np
import time
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output

class VirtualizationObj:

    def __init__(self):
        pass
    
    def setParams(self, maxPoint=[], minPoint=[]):
        self.maxPoint = maxPoint
        self.minPoint = minPoint

    def analyzeColor(self, color1):
        im1 = pyautogui.screenshot('modules/virtualization/libs/image.png')
        time.sleep(3)
        im = cv2.imread('modules/virtualization/libs/image.png')

        #rgb2bgr
        thisarr = []
        thisarr.append(color1[2])
        thisarr.append(color1[1])
        thisarr.append(color1[0])

        Y,X = np.where(np.all(im==thisarr, axis=2))
        indexesX = []
        indexesY = []

        if len(self.maxPoint) > 0 and len(self.minPoint) > 0:
            for i in X:
                if i > self.minPoint[0] and i < self.maxPoint[0]:
                    pass
                else:
                    indexesX.append(i)

            for i in Y:
                if i > self.minPoint[1] and i < self.maxPoint[1]:
                    pass
                else:
                    indexesY.append(i)

        if len(indexesX) > 0 and len(indexesY) > 0:
            X2 = np.setdiff1d(X, indexesX)
            Y2 = np.setdiff1d(Y, indexesY)
            finalTup = list(zip(X2,Y2))

            p = np.column_stack(finalTup)
            if len(p[0]) == 0 or len(p[1]) == 0:
                c = "Color not found"
            else:
                c = sum(p[0]) / len(p[0]), sum(p[1]) / len(p[1])

            return c

        else:

            p = np.column_stack((X,Y))

            if len(p) == 0:
                c = "Color not found"
            else:
                c = int(sum(X) / len(p)), int(sum(Y) / len(p))

            return c

    def analyzeWord(self, wordToSearch):

        im1 = pyautogui.screenshot('modules/virtualization/libs/image.png')
        pytesseract.pytesseract.tesseract_cmd = r'modules/virtualization/libs/tesseract/tesseract.exe'
        
        if len(self.minPoint) > 0 and len(self.maxPoint) == 0:
            im2 = cv2.imread('modules/virtualization/libs/image.png')
            self.maxPoint.append(im2.shape[:2][1])
            self.maxPoint.append(im2.shape[:2][0])
        
        if len(self.minPoint) == 0 and len(self.maxPoint) > 0:
            self.minPoint.append(0)
            self.minPoint.append(0)
        
        try:
            im1 = im1.crop(tuple(self.minPoint + self.maxPoint))
        except:
            pass
        
        im1.save("modules/virtualization/libs/cropImage.png")
        a = pytesseract.image_to_data(im1).replace("\t", " ").split("\n")
        # print(a)
        
        b = []
        for each in a:
            b.append(each.split(" "))

        c = []
        # e = encontrado?
        e = 0

        for cada in b:
            if e != 1:
                try:
                    cada.index(wordToSearch)
                    if len(self.minPoint) > 0:
                        c.append(int(float(self.minPoint[0]) + float(cada[6]) + (float(cada[8]) /2 )))
                        c.append(int(float(self.minPoint[1]) + float(cada[7]) + (float(cada[9]) /2 )))
                        # print(c) # descomentar para ver lo que lee el ocr
                    else:
                        c.append(int( float(cada[6]) + ((float(cada[8]) / 2))))
                        c.append(int( float(cada[7]) + ((float(cada[9]) / 2))))
                    e = 1
                except:
                    pass
        
        if len(c) < 1:
            c = "Word not found"
        
        return c

    def makeAClick(self, coordinates):
        pyautogui.moveTo(int(coordinates[0]), int(coordinates[1]))
        pyautogui.click()
