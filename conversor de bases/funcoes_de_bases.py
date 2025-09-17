def DecimalParaBinario(decimal):
    binario = ''
    num = int(decimal)
    while num > 0:
        resto = num % 2
        binario = str(resto) + binario
        num //= 2
    return binario
        
def DecimalParaOctal(decimal):
    octal = ''
    num = int(decimal)
    if num > 1:
        while num > 0:
            resto = num % 8
            octal = str(resto) + octal
            num //= 8
        return octal
        
def DecimalParaHexa(decimal):
    letras = ['A', ' B', 'C', 'D', 'E', 'F']
    hexa = ''
    num = int(decimal)
    if num > 1:
        while num > 0:
            resto = num % 16
            if resto == 10:
                hexa = str(letras[0]) + hexa
            elif resto == 11:
                hexa = str(letras[1]) + hexa
            elif resto == 12:
                hexa = str(letras[2]) + hexa
            elif resto == 13:
                hexa = str(letras[3]) + hexa
            elif resto == 14:
                hexa = str(letras[4]) + hexa
            elif resto == 15:
                hexa = str(letras[5]) + hexa
            else:
                hexa = str(resto) + hexa
            num //= 16
        return hexa
    
def BinarioParaDecimal(binario):
    decimal = 0
    bits = len(binario) -1
    for i in binario:
        calculo = (2**bits) * int(i)
        decimal += calculo
        bits -= 1
    return decimal

def OctalParaDecimal(octal):
    decimal = 0
    bits = len(octal) -1
    for i in octal:
        calculo = (8**bits) * int(i)
        decimal += calculo
        bits -= 1
    return decimal

def HexaParaDecimal(hexa):
    decimal = 0
    bits = len(hexa) -1
    for i in hexa:
        if i == 'A':
            calculo = (16**bits) * 10
            decimal += calculo
            bits -= 1
        elif i == 'B':
            calculo = (16**bits) * 11
            decimal += calculo
            bits -= 1
        elif i == 'C':
            calculo = (16**bits) * 12
            decimal += calculo
            bits -= 1
        elif i == 'D':
            calculo = (16**bits) * 13
            decimal += calculo
            bits -= 1
        elif i == 'E':
            calculo = (16**bits) * 14
            decimal += calculo
            bits -= 1
        elif i == 'F':
            calculo = (16**bits) * 15
            decimal += calculo
            bits -= 1
        else:
            calculo = (16**bits) * int(i)
            decimal += calculo
            bits -= 1
    return decimal

def BinarioParaOctal(binario):
    oc = DecimalParaOctal(BinarioParaDecimal(binario))
    return oc
    
def BinarioParaHexa(binario):
    he = DecimalParaHexa(BinarioParaDecimal(binario))
    return he
    
def HexaParaBinario(hexa):
    bi = DecimalParaBinario(HexaParaDecimal(hexa))
    return bi
    
def HexaParaOctal(hexa):
    he = DecimalParaOctal(HexaParaDecimal(hexa))
    return he

def OctalParaBinario(octal):
    oc = DecimalParaBinario(OctalParaDecimal(octal))
    return oc

def OctalParaHexa(octal):
    oc = DecimalParaHexa(OctalParaDecimal(octal))
    return oc