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

    def analyzeColor(self, color):
        im1 = pyautogui.screenshot('modules/virtualization/libs/image.png')
        time.sleep(3)
        im = cv2.imread('modules/virtualization/libs/image.png')
        # print(im)
        # color2 = [255,0,0]
        Y,X = np.where(np.all(im==color, axis=2))
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

    
    


# if __name__ == "__main__":
    

#     pytesseract.pytesseract.tesseract_cmd = r'tesseract/tesseract.exe'
#     # im1 = pyautogui.screenshot('asd.png')
#     a = pytesseract.image_to_data(Image.open('asd.png')).replace("\t", " ").split("\n")
#     print(a)
    

#     # img = cv2.imread('asd.png')
#     # d = pytesseract.image_to_data(img, output_type=Output.DICT)
#     # print(d)
#     # n_boxes = len(d['level'])
#     # for i in range(n_boxes):
#     #     (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#     b = []
#     for each in a:
#         b.append(each.split(" "))

#     print(a)
#     print(type(a))
#     print(b)
#     # print(b[3][7])
    
#     c = []
#     e = 0

#     for cada in b:
#         # print(cada)
#         if e != 1:
#             try: 
#                 print(cada.index("webpro"))
#                 print(cada)
#                 print(c)
#                 print(cada[7])
#                 print(cada[8])
#                 print(cada[9])
#                 print(cada[10])
#                 print("primer append")
#                 ques = int(cada[8]) + int(float(cada[10]))
#                 print(ques)
#                 print(int((int(float(cada[8])) + int(float(cada[10]))) / 2))
#                 c.append(int((float(cada[8]) + float(cada[10])) ))
#                 print("segundo append")
#                 c.append(int((float(cada[7]) + float(cada[9])) ))
#                 e = 1
#                 print(e)
#                 print("viene c")
#                 print(c)
#             except:
#                 pass
#     # print(b.index("Abbyy_Vantagezip"))
    
#     # print(pytesseract.image_to_data(Image.open('thisIsIt.png')))
#     pyautogui.moveTo(int(c[0]), int(c[1]))

#     # pyautogui.click()


#     #  --------------------------------  #

#     # im1 = pyautogui.screenshot('asd.png')

#     # im = cv2.imread('C:/Users/Caleb/Documents/Rocketbot_20201230_a4_win/Rocketbot/modules/virtualization/libs/asd.png')
#     # # im = np.asarray(im1)
#     # # print(im)
#     # minPoint = [0, 0]
#     # maxPoint = [1500, 1500]
#     # blue = [255,0,0]
#     # # print(np.where(np.all(im==blue, axis=2)))
#     # Y,X = np.where(np.all(im==blue, axis=2))
#     # # print("viene x")
#     # # print(X)
#     # indexesX = []
#     # for i in X:
#     #     if i > minPoint[0] and i < maxPoint[0]:
#     #         print("esta en los dos parametros")
#     #     else:
#     #         print("No esta en parametro")
#     #         print(i)
#     #         indexesX.append(i)
#     #         # print(X)
#     # indexesY = []
#     # for i in Y:
#     #     if i > minPoint[1] and i < maxPoint[1]:
#     #         print("esta en los dos parametros")
#     #     else:
#     #         print("No esta en parametro")
#     #         print(i)
#     #         indexesY.append(i)
#     #         print(X)
#     # # X3 = np.array(X)
#     # # print(X3)
#     # print("viene x")
#     # print(type(X))
#     # X2 = np.setdiff1d(X, indexesX)
#     # Y2 = np.setdiff1d(Y, indexesY)
#     # print("realX")
#     # print(type(X2))
#     # print(type(np.array(X2)))
#     # print("viene Y")
#     # print(Y2)
#     # print(sum(X2))
#     # print()
#     # finalTup = list(zip(X2,Y2))
#     # print(finalTup)
#     # # print(np.where(np.all(im==blue, axis=2)))
#     # p = np.column_stack(finalTup)
#     # c = sum(p[0]) / len(p[0]), sum(p[1]) / len(p[1])
#     # print("viene P")
#     # print(p)
#     # print(len(p[0]))
#     # print(len(p[1]))
#     # print(c)


#     # # print(p[0])
#     # # print(p[-1])

#     # # window_name = 'Image'

#     # # print(c[0])

#     # # d = c[0] + 10, c[1] + 10
#     # # print(d)

#     # # img2 = cv2.rectangle(im, pt1=(int(c[0]), int(c[1])), pt2=(int(d[0]), int(d[1])), color=(0,255,0), thickness=10)
#     # # img2 = cv2.rectangle(im, pt1=(Y[0],X[0]), pt2=(Y[-1],X[-1]), color=(0,255,0), thickness=10)

#     # # pt1=(p[0][0],p[0][1]), pt2=(p[-1][0],p[-1][1])

#     # # cv2.imwrite('thisIsIt.png', img2)
#     # pyautogui.moveTo(int(c[0]), int(c[1]))

#     # pyautogui.click()
    


