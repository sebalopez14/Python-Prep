while True:
    inp = int(input("ingresa numero: "))
    primo = True
    if inp > 2:
        for d in range(2,inp):
            if inp % d == 0:
                primo = False
        if (primo):
            print(inp, "es primo")
        else:
            print(inp, "no es primo")
    else:
        print("debe ingresar un numero mayor que 2!")