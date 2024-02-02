def ClaseAnimal(especie, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Animal, 
    la cual debe tener los siguientes atributos:
        Edad    (Un valor de tipo de dato entero, que debe inicializarse en cero)
        Especie (Un valor de tipo de dato string)
        Color   (Un valor de tipo de dato string)
    y debe tener el siguiente método:
        CumplirAnios  (este método debe sumar uno al atributo Edad y debe devolver ese valor)
    Recibe dos argumento:
        especie: Dato que se asignará al atributo Especie del objeto de la clase Animal
        color: Dato que se asignará al atributo Color del objeto de la clase Animal
    Ej:
        a = ClaseAnimal('perro','blanco')
        a.CumpliAnios() -> debe devolver 1
        a.CumpliAnios() -> debe devolver 2
        a.CumpliAnios() -> debe devolver 3
    '''
    #Tu código aca:
    
    class Animal:
        def __init__(self, especie, color ,edad=0):
            self.Edad = edad
            self.Especie = especie
            self.Color = color
        
        def __str__(self):
            return f"{self.Especie ,self.Color,self.Edad}"
        
        def CumpliAnios(self):
            self.Edad += 1
            print(self.Edad)
    
    animal = Animal(especie, color)
    return animal

a = ClaseAnimal('perro','blanco')
print(a)
a.CumpliAnios()
a.CumpliAnios()
a.CumpliAnios()