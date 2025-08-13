#E: numero
#S: cantidad de digitos del numero
#R: entero, positivo
def digitos(num):
    if not isinstance(num,int):
        return "Error: entrada debe ser entera"
    if not num >0:
        return "Error: entrada debeb ser positiva"
    if not num > 9:
        return 1
    cont = 0
    while num>0:
        cont += 1
        num //= 10
    return cont
#E:numero
#S: la suma total de los digitos del numero
#R: entero, positivo
def suma_digitos(num):
    if not isinstance(num,int):
        return "Error: entrada debe ser entera"
    if not num >0:
        return "Error: entrada debeb ser positiva"
    if not num > 9:
        return num
    res = 0
    while num>0:
        res += num%10
        num //= 10
    return res
#E: numero
#S: retorna la cantidad de multiplos de 3 en el numero
#R: entero, positivo
def multiplos_3(num):
    if not isinstance(num,int):
        return "Error: entrada debe ser entera"
    if not num >0:
        return "Error: entrada debeb ser positiva"
    res = 0
    div = 1
    while num>=div:
        if div%3 == 0:
            res += 1
            div += 1
        else:
            div += 1
    return res
#
#
#
def palindromo(num):
    if not isinstance(num,int):
        return "Error: entrada debe ser entera"
    if not num >0:
        return "Error: entrada debeb ser positiva"
    lar = digitos(num)
    temp = num%(10**(lar//2))
    lar-=1
    while temp>0:
        if temp%10 == num//(10**lar):
            temp = temp//10
            num = num%(10**lar)
            lar-= 1
        else:
            return False
    return True 
#
#
#
def primo(num):
    if num < 0:
        return False
    else:
        div = 0
        while div<num:
            if num%div == 0:
                return False
            else:
                div += 1
        return True

def intercambiar(n1, n2):
    res = 0
    exp = 0
    while n1>0:
        dig1 = n1%10
        dig2 = n2%10
        if primo(dig1+dig2):
            res += dig2*(10**exp)
        else:
            res += dig1*(10**exp)
        n1 = n1//10
        n2 = n2//10
        exp += 1
    return res

