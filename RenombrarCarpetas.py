#!/usr/bin/env python
# coding: utf-8

import os ## Manejo de sistema operativo
import re ## Regular expresion

path = input("ingresa la ruta: ")
files = os.listdir(path)

nombres = []
extension = []
for x in files:
    nombres.append(os.path.splitext(x)[0])
    extension.append(os.path.splitext(x)[1])

nombresa = [re.sub('[^0-9]+', '', x)for x in nombres]##selecciona solo letras en minusculas y mayusculas

i = int (1)
for i in range(len(files)):
    os.rename(path + chr(92) + files[i], path + chr(92) + nombresa[i])
