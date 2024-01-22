#Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
n = 100
while n<300:
    if n % 3 == 0 and n % 6 == 0:
        print(n)
        break
    else:
        n += 1