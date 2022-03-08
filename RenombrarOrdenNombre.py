#!/usr/bin/env python
# coding: utf-8

# In[117]:


##Modifica los nombres de una carpeta especifica segun el path
##Maximo 40 caracteres, Primera letra en mayuscula, asigna consecutivo
##de 4 digitos, elimina los caracteres especiales y espacios
##Asigna el nombre "Documentoelectronico" a los nombres vacios
##Realiza las modificaciones segun la fecha de modificacion
##Verifica si es carpeta


# In[1]:


import os ## Manejo de sistema operativo
import re ## Regular expresion

import sys, time
import glob
ruta = input("ingresa la ruta: ")


# In[3]:


files = os.listdir(ruta)
#print(files)

##files = sorted(files, key = lambda x: os.path.getmtime(os.path.join(ruta, x)))

#print(files)


# In[17]:


nombres = []
extension = []
for x in files:
    ##condicional con isdir()
    if (os.path.isdir(ruta + chr(92) + x)):
        nombres.append(x)
        extension.append("")
        print("ingresa")
        continue
    nombres.append(os.path.splitext(x)[0])
    extension.append(os.path.splitext(x)[1])
nombres = [i.title() for i in nombres]
#print(nombres)
#print(extension)


# In[18]:


nombresa = [re.sub('[^a-zA-Z]+', '', x)for x in nombres]##selecciona solo letras en miubnusculas y mayusculas
nombresc = []

""" print(nombresa)
print()
print(nombresc)
print() """

for z in nombresa:
    nombresc.append(z[0:36])
#print(nombresc)


# In[19]:


for i in range(len(nombresc)):
    #print(i)
    if nombresc[i] == "":
        #print(nombresc)
        
        nombresc[i] = ("Documentoelectronico")
        
        #print(nombresc)
#print(nombresc)


# In[20]:


numeracion = [f"{x:04}"for x in range(1,len(nombresc)+1)]
#print(numeracion)


# In[21]:


concat = list(map(''.join, zip(numeracion,nombresc)))
concat2 = list(map(''.join, zip(concat,extension)))
#print (concat2)


# In[22]:

print(files)
print()
print(concat2)

for i in range(len(files)):
    try:   
        os.rename(ruta + chr(92) + files[i], ruta + chr(92) + concat2[i])
    except:
        import string
        import random
        number_of_strings = 3
        length_of_string = 3
        os.rename(ruta + chr(92) + files[i], ruta + chr(92) + os.path.splitext(concat2[i])[0] + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)) + os.path.splitext(concat2[i])[1])

