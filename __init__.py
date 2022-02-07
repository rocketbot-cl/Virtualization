# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys
# import pytesseract
# from pytesseract import Output

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'virtualization' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


import pyautogui
import time
from virtualizationObj import VirtualizationObj

global virtualization_I


module = GetParams("module")

try:

    if (module == "searchColor"):

        virtualization_I = VirtualizationObj()

        maxPoint = GetParams("maxPoint")
        if (maxPoint == None or maxPoint == ""):
            maxPoint = []
        else:
            maxPoint = eval(maxPoint)
        
        minPoint = GetParams("minPoint")
        if (minPoint == None or minPoint == ""):
            minPoint = [0,0]
        else:
            minPoint = eval(minPoint)
        
        virtualization_I.setParams(maxPoint, minPoint)

        colors = GetParams("iframe")
        firstColor = eval(colors)["firstColor"]
        firstColor = hex_to_rgb(firstColor)
        result = virtualization_I.analyzeColor(firstColor)

        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, result)

    if (module == "clickOnColor"):

        virtualization_I = VirtualizationObj()

        maxPoint = GetParams("maxPoint")
        if (maxPoint == None or maxPoint == ""):
            maxPoint = []
        else:
            maxPoint = eval(maxPoint)
        
        minPoint = GetParams("minPoint")
        if (minPoint == None or minPoint == ""):
            minPoint = [0,0]
        else:
            minPoint = eval(minPoint)
        
        virtualization_I.setParams(maxPoint, minPoint)
        
        colors = GetParams("iframe")
        firstColor = eval(colors)["firstColor"]
        firstColor = hex_to_rgb(firstColor)
        
        result = virtualization_I.analyzeColor(firstColor)
        
        if (result != "Color not found"):
            clickOption = GetParams("clickOption")
            if clickOption == "singleClick":
                virtualization_I.makeAClick(result)
            
            if clickOption == "doubleClick":
                virtualization_I.makeADoubleClick(result)
                
            if clickOption == "singleRightClick":
                virtualization_I.makeAsingleRightClick(result)
            
            if clickOption == "doubleRightClick":
                virtualization_I.makeAdoubleRightClick(result)

            if clickOption == "singleMiddleClick":
                virtualization_I.makeAsingleMiddleClick(result)
            
            if clickOption == "doubleMiddleClick":
                virtualization_I.makeAdoubleMiddleClick(result)
            result = True
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, result)

    if (module == "searchWord"):

        virtualization_I = VirtualizationObj()

        maxPoint = GetParams("maxPoint")
        if (maxPoint == None or maxPoint == ""):
            maxPoint = []
        else:
            maxPoint = eval(maxPoint)
        
        minPoint = GetParams("minPoint")
        if (minPoint == None or minPoint == ""):
            minPoint = [0,0]
        else:
            minPoint = eval(minPoint)

        virtualization_I.setParams(maxPoint, minPoint)

        word = GetParams("word")
        result = virtualization_I.analyzeWord(word, path_tesseract)
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, result)

    if (module == "clickOnWord"):

        virtualization_I = VirtualizationObj()

        maxPoint = GetParams("maxPoint")
        if (maxPoint == None or maxPoint == ""):
            maxPoint = []
        else:
            maxPoint = eval(maxPoint)
        
        minPoint = GetParams("minPoint")
        if (minPoint == None or minPoint == ""):
            minPoint = [0,0]
        else:
            minPoint = eval(minPoint)

        virtualization_I.setParams(maxPoint, minPoint)

        word = GetParams("word")
        result = virtualization_I.analyzeWord(word, path_tesseract)

        try:

            result2 = (int(result["x"]) + int(result["width"] / 2),int(result["y"]) + int(result["height"] / 2))
        except:
            result2 = False

        if (result2 != False):
            clickOption = GetParams("clickOption")
            if clickOption == "singleClick":
                virtualization_I.makeAClick(result)
            
            if clickOption == "doubleClick":
                virtualization_I.makeADoubleClick(result)
                
            if clickOption == "singleRightClick":
                virtualization_I.makeAsingleRightClick(result)
            
            if clickOption == "doubleRightClick":
                virtualization_I.makeAdoubleRightClick(result)

            if clickOption == "singleMiddleClick":
                virtualization_I.makeAsingleMiddleClick(result)
            
            if clickOption == "doubleMiddleClick":
                virtualization_I.makeAdoubleMiddleClick(result)
            result2 = True
        
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, result2)
    


except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e