numeros = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 3, 10, 2, 2, 3, 3, 3, 4, 4, 4, 4]

def de_lista_a_dicc(x):
    dicc_repes= {}
    for i in x:
        if i in dicc_repes:
            continue
        contador = 0
        for e in x:
            if i == e:
                contador += 1
        dicc_repes[i] = contador
    return dicc_repes

def elem_mas_repite_dicc(dicc):
    valormayor = 0
    for i in dicc:
        valor = dicc[i]
        if valor > valormayor:
            clavedelmayor = i
            valormayor = valor
    print("El numero que mas se repite es ", clavedelmayor, ",",valormayor," veces")
    
    for i in dicc:
        valor = dicc[i]
        if valor == valormayor and i != clavedelmayor:
            print("Empata en cantidad con ", i, ",que se repite ",valormayor," veces")


diccionario = de_lista_a_dicc(numeros)
print(diccionario)
elem_mas_repite_dicc(diccionario)


lista_strings = ["verde" ,"verde" ,"verde" , "rojo", "azul", "azul"]

diccionario = de_lista_a_dicc(lista_strings)
print(diccionario)
elem_mas_repite_dicc(diccionario)
