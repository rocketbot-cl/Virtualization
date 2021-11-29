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

def ocr_image(img_):
    """
    OCR the image and return the text with coordinates.

    :param img_: Image to OCR
    :param to_data: Return the text with data
    :return str | dict: Text or data with coordinates

    """
    try:
        # if _platform == "linux" or _platform == "linux2":
        #     pass
        # elif _platform == "darwin":
        #     pytesseract.pytesseract.tesseract_cmd = path_tesseract.mac
        # elif _platform == "win32":
        #     pytesseract.pytesseract.tesseract_cmd = path_tesseract.win
        pytesseract.pytesseract.tesseract_cmd = r'modules/virtualization/libs/tesseract/tesseract.exe'

        ocr = pytesseract.image_to_data(img_, lang="spa", output_type=pytesseract.Output.DICT)
        
        return ocr
    except Exception as e:
        print("exception ocr_image")
        print(e)
    return None

def find_text_in_data(data_img, text):
    """
    Return the coordinates of the text in the image data.

    :param data_img: OCR image as data
    :param text: Text to search
    :return: Coordinates of the text or None
    """
    try:
        for i in range(len(data_img['level'])):
            if data_img['text'][i] == text:
                return {
                    "x":data_img['left'][i], 
                    "y": data_img['top'][i],
                    "width":data_img['width'][i], 
                    "height": data_img['height'][i]
                }
        return None
    except Exception as e:
        print("exception find_text_in_data")
        print(e)
        return None

def find_text_in_image(img__, text):
    """
    Return the coordinates of the text in the image.

    :param img__: Image where to search
    :param text: Text to search
    :return: Coordinates of the text or None
    """
    try:
        for j in range(3,1,-1):
            for i in range(0, j):
                print(j, "Searching text", text)
                x = i*img__.width/j
                img_cropped = __edit_image(img__, scale=3, crop=(x, 0, x+img__.width/j, img__.height))
                ocr_img = ocr_image(img_cropped)
                coord = find_text_in_data(ocr_img, text)
                if coord:
                    return {
                        "x":coord["x"]/3 + x,
                        "y": coord["y"]/3,
                        "width": coord["width"]/3,
                        "height": coord["height"]/3
                    }
                
    except Exception as e:
        print("exception find_text_in_image")
        print(e)
 
    return None

def __edit_image(img, scale=1, crop=None):
    img = img.resize((int(img.width*scale), int(img.height*scale)), Image.ANTIALIAS)
    if crop:
        img.crop(crop)
    
    return img

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
        # thisIsOrc = ocr_image()
        # pytesseract.pytesseract.tesseract_cmd = r'modules/virtualization/libs/tesseract/tesseract.exe'
        
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

        # pytesseract.pytesseract.tesseract_cmd = r'modules/virtualization/libs/tesseract/tesseract.exe'
        return find_text_in_image(im1, wordToSearch)

    def makeAClick(self, coordinates):
        try:
            eval(coordinates)
        except:
            pass
        pyautogui.moveTo(int(coordinates[0]), int(coordinates[1]))
        pyautogui.click()
