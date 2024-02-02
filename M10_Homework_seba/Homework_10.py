import os
txt = f"""
import sys

if len(sys.argv) == 4:
    print("parametro 1:",sys.argv[1])
    print("parametro 2:",sys.argv[2])
    print("parametro 3:",sys.argv[3])
else:
    print("no ingreso 3 parametros ")"""
    
archivo = open("clase09_ej1.py", "w")
archivo.write(txt)
archivo.close()

