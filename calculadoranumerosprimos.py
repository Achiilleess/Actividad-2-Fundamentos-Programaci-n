#empezamos por definir todas las variables 
n : int
iteracion : int = 3

#solicitamos el numero al usuario
n = int(input("Ingrese numero: "))

#creamos un ciclo for que divida el numero ingresado por el usuario progresivamente hasta llegar al numero anterior al mismo (por eso la varible limite) 

if n == 2:
    #si n es igual a 2 se asume que es un número primo 
    print(n,"es primo")
elif n == 0:
    #si n es igual a 0 no es primo ni compuesto, pues no es divisible entre nada
    print(n, "no es primo ni compuesto")
elif n % 2 == 0:
    #si n se divide entre 2 sin dejar residuo alguno entonces es un número paar, y por ende no es primo
    print(n, "no es primo")
elif n < 1:
    #si n es menor que n, no puede ser primo
    print(n, "no es primo porque es menor que 1")
elif n != 2:
    # si n no es igual a 2 y no cumple con ninguna de las condiciones anteriores se debe utilizar el siguiente ciclo for para comprobar si es primo o no
    for iteracion in range(3, n):
        #este ciclo se encarga de probar dividir los primos desde 3 hasta el numero que ingresa el usuario (n) hasta llegar a uno que no deje residuo en la operacion (n no es primo) o comprobar que ninguno es divisor (n es primo)
        resultado = n % iteracion
        iteracion = iteracion + 2
        if resultado == 0:
            print(n,"no es primo")
            break
        elif resultado != 0:
            print(n,"es primo")
            break
