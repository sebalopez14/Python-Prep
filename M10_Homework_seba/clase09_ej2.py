import sys
import datetime
import os

fecha = datetime.datetime.now()
temperatura = input("temperatura: ")
humedad = input("porcentaje de humedad: ")
llovio = input("llovio si o no: ").lower()
if llovio == "si":
    llovio = "True"
elif llovio == "no":
    llovio = "False"
info = str(fecha) + "," + temperatura + "," + humedad + "," + llovio

archivo = open("clase09_ej2.csv", "a")
archivo.write(info+"\n")
archivo.close()
