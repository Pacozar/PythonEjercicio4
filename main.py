while True:
    try:
        Edad = int(input('¿Cuantos años tienes? \n'))
        break
    except:
        print('Edad no valida')
if Edad < 18:
    print('Eres menor de edad')
elif Edad >= 18:
    print('Eres mayor de edad')
