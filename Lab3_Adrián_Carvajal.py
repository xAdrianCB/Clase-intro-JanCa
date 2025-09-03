#E: n
#S: retorna n-1 + n-2 si n >1, 0 si n = 0 y 1 si n = 1.
#R: debe ser un numero entero
def fib(n):
    if not isinstance(n, int):
        return "Error: La entrada debe ser un número entero"
    if n!=0:
        if n>1:
            return fib(n-1) + fib(n-2)
        else:
            return 1
    else:
        return 0
    

#E: num
#S: retorna la resta entre la cantidad de pares e impares de num
#R: la entrada debe ser un número entero positivo
def par_impares(num):
    if not isinstance(num, int):
        return "Error: La entrada debe ser un número entero"
    if num < 0:
        return "Error: La entrada debe ser un número positivo"
    return largo_pares(num) - largo_impares(num)
#Aux
def largo_pares(num):
    res = 0
    while num > 0:
        if (num%10) % 2 == 0:
            res+= 1
        num//=10
    return res
def largo_impares(num):
    res = 0
    while num > 0:
        if (num%10) % 2 == 1:
            res+= 1
        num//=10
    return res
print(par_impares(841235))
print(par_impares(840112531))

#E: num
#S: retorna el numero gemelo primo si la entrada en un numero primo y tiene un gemelo primo
#R: entrada entera, positiva
def primo_gemelo(num):
    if not isinstance(num, int):
        return "Error: La entrada debe ser un número entero"
    if num < 0:
        return "Error: La entrada debe ser un número positivo"
    if esPrimo(num):
        if esPrimo(num+2):
            return num+2
        else:
            return "No tiene primo gemelo"
    else:
        return "El número ingresado no es primo"
#Aux
def esPrimo(num):
    if num == 1:
        return False
    div = 2
    while div != num:
        if num % div == 0:
            return False
        div+= 1
    return True
print(primo_gemelo(41))
print(primo_gemelo(25))
print(primo_gemelo(83))

#E: num, ini, fin
#S: un número formado desde la posición inicial hasta la posición final, se incluyen las posiciones.
#R: entrada entereo,positivo
def inicio_fin(num, ini, fin):
    if not isinstance(num, int):
        return "Error: La entrada debe ser un número entero"
    if num < 0:
        return "Error: La entrada debe ser un número positivo"
    if ini>fin:
        return "No es posible formar ese número"
    if fin>= largo(num):
        return "Las posiciones no son válidas"
    res = 0
    ini-= 1
    i = 0
    num = inverso(num)
    while ini != fin+1:
        if i >= ini and i != fin:
            res = (res*10) + num%10
        i += 1
    return res
def largo(num):
    if num<10:
        return 1
    cont = 0
    while num>0:
        cont+= 1
        num//=10
    return cont
def inverso(num):
    if num<9:
        return num
    res = 0
    while num>0:
        res = (res*10) + num%10
        num//=10
    return res

print(inicio_fin(3478743224,2,5))
print(inicio_fin(5281,6,2))
print(inicio_fin(19371,1,5))

        


