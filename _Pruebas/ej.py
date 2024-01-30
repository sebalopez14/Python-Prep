def grados_conver():
    valor = int(input("Ingrese los grados (numerico)"))
    orig = input("Elija la medida ingresada (C,F,K)")
    dest = input("Elija a que grado desea convertir: (C,F,K)")
    
    celsius_a_fahrenheit = (9/5) * valor + 32
    fahrenheit_a_celsius = (5/9) * (valor - 32)
    celsius_a_kelvin = valor + 273.15
    kelvin_a_celsius = valor - 273.15
    fahrenheit_a_kelvin = (5/9) * (valor - 32) + 273.15
    kelvin_a_fahrenheit = (9/5) * (valor - 273.15) + 32
    
    if orig == "c" and dest == "f":
        return celsius_a_fahrenheit
    elif orig == "f" and dest == "c":
        return fahrenheit_a_celsius
    elif orig == "c" and dest == "k":
        return celsius_a_kelvin
    elif orig == "k" and dest == "c":
        return kelvin_a_celsius
    elif orig == "f" and dest == "k":
        return fahrenheit_a_kelvin
    elif orig == "k" and dest == "f":
        return kelvin_a_fahrenheit

# print(grados_conver())


def factorial(num):
    if num >1:
        num = num * factorial(num-1)
    return num

print(factorial(5))