# Virtualizacion
  
Search for colors, words or coordinates and interact with them.  

*Read this in other languages: [English](Manual_virtualization.md), [Português](Manual_virtualization.pr.md), [Español](Manual_virtualization.es.md)*
  
![banner](imgs/Banner_virtualization.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module
In order to use this module, you have to pick a color or word to search for; and if you want to restrict the area to search in, insert the range of it.


## Description of the commands

### Search Color
  
Searchs for a color in the screen
|Parameters|Description|example|
| --- | --- | --- |
|Minimum point|Minimum point to search in.|[0, 0]|
|Maximum point|Maximum point to search in.|[1500, 1500]|
|Pick color|Color to search in the screen|#ffffff|
|Assign result to variable|Variable where the result of the search will be stored.|Variable|

### Click on color
  
Searchs for a color in the screen
|Parameters|Description|example|
| --- | --- | --- |
|Minimum point|Minimum point to search in.|[0, 0]|
|Maximum point|Maximum point to search in.|[1500, 1500]|
|Pick color|Pick the color that you want to click.|#ffffff|
|Assign result to variable|Name of the variable where the result will be stored.|Variable|
|Type of click|Type of click that you want to perform.|singleClick|

### Search a word
  
Searchs for a word in the screen
|Parameters|Description|example|
| --- | --- | --- |
|Minimum point|Minimum point to search in.|[0, 0]|
|Maximum point|Maximum point to search in.|[1500, 1500]|
|Word to search|Word you want to search for.|word|
|Assign result to variable|Name of the variable in which the result will be saved.|Variable|

### Click on word
  
Searchs for a word in the screen
|Parameters|Description|example|
| --- | --- | --- |
|Minimum point|Minimum point to search in. \| Leave empty if you do not need minimum.|[0, 0]|
|Maximum point|Maximum point to search in. \| Leave empty if you do not need maximum.|[1500, 1500]|
|Word to search|Word you want to search for.|word|
|Assign result to variable|Name of the variable where the result will be stored.|Variable|
|Type of click|Type of click that you want to perform.|singleClick|

### Click on hold
  
This command allows you to click on hold on a specific position of the screen for a specific time.
|Parameters|Description|example|
| --- | --- | --- |
|Position X|Position X to click.|300|
|Position Y|Position Y to click.|300|
|Duration in seconds|Duration in seconds of the click hold.|10|
