# Virtualization
  
Busca colores, palabras o coordenadas e interactua con ellos.  

*Read this in other languages: [English](Manual_virtualization.md), [Português](Manual_virtualization.pr.md), [Español](Manual_virtualization.es.md)*
  
![banner](imgs/Banner_virtualization.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este módulo
Para usar este módulo, tienes que proporcionar un color o palabra a buscar, y opcionalmente puedes elegir el
rango en el cual hacerlo (caso contrario, será toda la pantalla).



## Descripción de los comandos

### Buscar Color
  
Busca un color en la pantalla
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Punto mínimo|Punto mínimo en el cual buscar.|[0, 0]|
|Punto máximo|Punto maximo en el cual buscar.|[1500, 1500]|
|Seleccione el color|Color a buscar en la pantalla|#ffffff|
|Asignar resultado a variable|Variable donde se almacenará el resultado de la búsqueda.|Variable|

### Click en color
  
Busca un color en la pantalla
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Punto mínimo|Punto mínimo en el cual buscar.|[0, 0]|
|Punto máximo|Punto maximo en el cual buscar.|[1500, 1500]|
|Seleccione el color|Seleccione el color que desea clickear.|#ffffff|
|Asignar resultado a variable|Nombre de la variable donde se almacenará el resultado.|Variable|
|Tipo de click|Tipo de click que se desea ejecutar.|singleClick|

### Buscar una palabra
  
Busca una palabra en la pantalla
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Punto mínimo|Punto mínimo en el cual buscar.|[0, 0]|
|Punto máximo|Punto maximo en el cual buscar.|[1500, 1500]|
|Palabra a buscar|Palabra que se desea buscar.|palabra|
|Asignar resultado a variable|Nombre de la variable en la cual se guardará el resultado.|Variable|

### Click en palabra
  
Busca una palabra en la pantalla
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Punto mínimo|Punto mínimo en el cual buscar. \| Dejar en blanco para tomar toda la pantalla.|[0, 0]|
|Punto máximo|Punto maximo en el cual buscar. \| Dejar en blanco para tomar toda la pantalla.|[1500, 1500]|
|Palabra a buscar|Palabra que se desea buscar.|palabra|
|Asignar resultado a variable|Nombre de la variable en la cual se guardará el resultado.|Variable|
|Tipo de click|Tipo de click que se desea ejecutar.|singleClick|

### Click sostenido
  
Este comando permite hacer click sostenido en una posición específica de la pantalla por un tiempo específico.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Posición X|Posición X en la que hacer click.|300|
|Posición Y|Posición Y en la que hacer click.|300|
|Duración en segundos|Duración en segundos del click sostenido.|10|
