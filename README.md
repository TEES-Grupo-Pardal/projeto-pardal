# projeto-pardal

## Overview
Reposotório a fim de realizar parte a tarefa de, dado imagens e suas respectivas coordendas, ele trata a imagem e recorta segundo as coordenadas disponíveis em arquivos txts. <br></br>
Depois da imagem tratada, ela é submetida ao tesseract que extrai os caracteres contidos na imagem.
Por fim, armazena em um mini Banco de Dados, com apenas uma tabela, mas que armazena tupla do resultado do tesseract: A imagem em si, as coordenadas, a imagem tratada e os caracteres extraidos pelo tesseract. <br></br>
O repositório está com testes para a extração de caracteres de placas de veículos. <br></br>

## Arquitetura do repositório

|--------------- db ------------- banco.py (Funções para o uso do Banco de Dados, criar um Banco, Criar tabela, Inserir dados, commitar, etc);</br>
|----------- gray-mages --------- Diretório onde ficaram as imagens tratadas (geradas automáticamente após a execução do script);</br>
|--------------- obj ------------ Diretório onde ficam as imagens e seus respectivos txts;</br>
|-------------- plates ---------- Diretório onde ficaram as imagens das placas tratadas (geradas automáticamente após a execução do script);</br>
|------- script-process.py------- Script onde faz todo o processo: trata a imagem, passa pelo tesseract e armazena no db.</br>

## Executar o projeto
```
pip install -r .\requirements.txt
python .\image-process\script-process.py
```
## Integrantes
|      Nome       |           email          |
|:---------------:|:------------------------:|
| Fernando Vargas |  nandovargas7@gmail.com  |
|  Luis Guilherme | luis.ggaboardi@gmail.com |
|   Vitor Yukio   |   yukio.link@gmail.com   |
