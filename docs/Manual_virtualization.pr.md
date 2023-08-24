# Virtualization
  
Procure por cores, palavras ou coordenadas e interaja com eles.  

*Read this in other languages: [English](Manual_virtualization.md), [Português](Manual_virtualization.pr.md), [Español](Manual_virtualization.es.md)*
  
![banner](imgs/Banner_virtualization.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  







## Descrição do comando

### Buscar Cor
  
Busca uma cor na tela
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Ponto mínimo|Ponto mínimo para procurar.|[0, 0]|
|Ponto máximo|Ponto máximo para procurar.|[1500, 1500]|
|Selecione a cor|Cor para procurar na tela|#ffffff|
|Atribuir resultado à variável|Variável onde o resultado da busca será armazenado.|Variável|

### Clique na cor
  
Procura uma cor na tela
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Ponto mínimo|Ponto mínimo para procurar.|[0, 0]|
|Ponto máximo|Ponto máximo para procurar.|[1500, 1500]|
|Selecione a cor|Selecione a cor que deseja clicar.|#ffffff|
|Atribuir resultado à variável|Nome da variável onde o resultado será armazenado.|Variável|
|Tipo de clique|Tipo de clique que deseja executar.|singleClick|

### Buscar uma palavra
  
Busca uma palavra na tela
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Ponto mínimo|Ponto mínimo para procurar.|[0, 0]|
|Ponto máximo|Ponto máximo para procurar.|[1500, 1500]|
|Palavra para procurar|Palavra que você deseja procurar.|palavra|
|Atribuir resultado à variável|Nome da variável na qual o resultado será salvo.|Variável|

### Click on word
  
Searchs for a word in the screen
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Ponto mínimo|Ponto mínimo para pesquisar. \| Deixe em branco para pegar toda a tela.|[0, 0]|
|Ponto máximo|Ponto máximo para pesquisar. \| Deixe em branco para pegar toda a tela.|[1500, 1500]|
|Palavra a pesquisar|Palavra que você deseja pesquisar.|palavra|
|Atribuir resultado à variável|Nome da variável na qual o resultado será salvo.|Variável|
|Tipo de clique|Tipo de clique que você deseja executar.|singleClick|

### Clicar sem soltar
  
Este comando permite clicar sem soltar em uma posição específica da tela por um tempo específico.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Posição X|Posição X para clicar.|300|
|Posição Y|Posição Y para clicar.|300|
|Duração em segundos|Duração em segundos do clique sem soltar.|10|
