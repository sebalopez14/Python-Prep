class Funciones:
    def __init__(self, l):
        self.lista = l
        
    def mostrar_lista(self):
        print(self.lista)
    
    def primo(self,x) :
        es_primo=True
        for i in range(2,x):
            if x % i == 0:
                es_primo =  False
        return es_primo
    
    def valor_modal(lista): #La tome de la solucion ya que resolvi este ejercicio del modulo anterior de otra manera
        lista_unicos = []
        lista_repeticiones = []
        if len(lista) == 0:
            return None
        for elemento in lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def grados_conver(valor, orig, dest):
    
        celsius_a_fahrenheit = (9/5) * valor + 32
        fahrenheit_a_celsius = (5/9) * (valor - 32)
        celsius_a_kelvin = valor + 273.15
        kelvin_a_celsius = valor - 273.15
        fahrenheit_a_kelvin = (5/9) * (valor - 32) + 273.15
        kelvin_a_fahrenheit = (9/5) * (valor - 273.15) + 32
        
        if orig == "celsius" and dest == "farenheit":
            return celsius_a_fahrenheit
        elif orig == "farenheit" and dest == "celsius":
            return fahrenheit_a_celsius
        elif orig == "celsius" and dest == "kelvin":
            return celsius_a_kelvin
        elif orig == "kelvin" and dest == "celsius":
            return kelvin_a_celsius
        elif orig == "farenheit" and dest == "kelvin":
            return fahrenheit_a_kelvin
        elif orig == "kelvin" and dest == "farenheit":
            return kelvin_a_fahrenheit
        elif orig == dest:
            return "No se puede convertir en la misma medida"
        
    def factorial(self, n):
        if(type(n) != int or n<0):
            return "El numero debe ser un entero y positivo"
        if (n > 1):
            n = n * self.factorial(n - 1)
        return n
    
    def primo_lista(self):
        for i in self.lista:
            if (self.primo(i)):
                print(i, "Es primo")
            else:
                print(i, "No es primo")
                
    def grados_lista(self, ori, des):
        for i in self.lista:
            print(i, 'grados', ori, 'son', self.grados_conver(i, ori, des),'grados',des)

    def factorial_lista(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.factorial(i))