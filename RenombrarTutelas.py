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

nombresa = [re.sub('[^a-zA-Z]+', '', x)for x in nombres]##selecciona solo letras en miubnusculas y mayusculas

numeracion = [f"{x:03}"for x in range(1,len(nombresa)+1)]

concat = list(map(''.join, zip(numeracion,nombresa)))
concat2 = list(map(''.join, zip(concat,extension)))

for i in range(len(files)):
    try:   
        os.rename(path + chr(92) + files[i], path + chr(92) + concat2[i])
    except:
        import string
        import random
        number_of_strings = 3
        length_of_string = 3
        os.rename(path + chr(92) + files[i], path + chr(92) + os.path.splitext(concat2[i])[0] + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + os.path.splitext(concat2[i])[1])
