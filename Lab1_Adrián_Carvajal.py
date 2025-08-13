#E: un numero, digito
#S: el numero invertido hasta encontrar el digito
#R: num,dig debe ser enteros positivos/ dig debe ser entre 0 y 9/ num > 0
def invertir(num, dig):
    if not isinstance(num, int):
        return "Error: num debe ser entera"
    if not isinstance(dig, int):
        return "Error: dig debe ser entera"
    if dig>9 and dig<0:
        return "Error: dig debe estra en un rango de 0 a 9"
    if not num>0:
        return "Error: num debe ser mayor a 0"
    res = 0
    while num>0:
        if num%10 != dig:
            res = (res*10)+ num%10
            num //= 10
        else:
            return res
    return res

#E: num1 y num2
#S: retorna un número que corresponde a aquellos dígitos que
#están en el primer número pero no en el segundo número.
#R: num1, num2 deben ser eneteros positivos
def diferencia(num1, num2):
    if not isinstance(num1, int):
        return "Error: Números deben ser enteros"
    if not isinstance(num2, int):
        return "Error: Números deben ser enteros"
    if num1<0:
        return "Error: entrada deben ser positivos"
    if num2<0:
        return "Error: entrada deben ser positivos"
    res = 0
    exp = 0
    while num1>0:
        if econtrar_num(num2, num1%10):
            res += (num1%10)*(10**exp)
            exp += 1
        num1 //= 10
    return res
#Aux
def encontrar_num(num, dig):
    while num>0:
        if num%10 == dig:
            return False
        num//= 10
    return True    
#E: un numero
#S: retorna un numero conformadopor los digito mayor de entre lo posibles grupos de 3 de los 12 digitos del numero.
#R: num debe ser de 12 digitos, entero y positivo
def agrupar_mayores(num):
    if not isinstance(num, int):
        return "Error: La entrada deben ser un numero entero"
    if num<0:
        return "Error: La entrada deben ser un numero positivo"
    if num<999999999999 and num>9999999999999:
        return "Error: La entrada debe ser un numero de 12 digitos"
    
    res = 0
    exp = 0
    while num>0:
        res += (dig_mayor(num%1000))*(10**exp)
        exp += 1
        num //= 1000
    return res
#Aux
def dig_mayor(num):
    ult = num%10
    num //= 10
    while num>0:
        if num%10 >= ult:
            ult = num%10
        num //= 10
    return ult
