import funcoes_de_bases as conv

def main():
    while True:
        print("\n===== Conversor de Bases Numéricas =====")
        print("Opções de bases: ")
        print("1 - Decimal")
        print("2 - Binário")
        print("3 - Octal")
        print("4 - Hexadecimal")
        print("-1 - Encerrar programa")

        try:
            entrada = int(input("\nEscolha a base de entrada (1 a 4 ou -1 para sair): "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if entrada == -1:
            print("Encerrando o programa... Até mais!")
            break  

        if entrada not in [1, 2, 3, 4]:
            print("Opção inexistente para base de entrada.")
            continue  

        try:
            saida = int(input("Escolha a base de saída (1 a 4): "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if saida not in [1, 2, 3, 4]:
            print("Opção inexistente para base de saída.")
            continue  

        numero = input("Digite o número: ")

        resultado = None

        if entrada == 1: 
            if saida == 2:
                resultado = conv.DecimalParaBinario(numero)
            elif saida == 3:
                resultado = conv.DecimalParaOctal(numero)
            elif saida == 4:
                resultado = conv.DecimalParaHexa(numero)
            else:
                resultado = numero

        elif entrada == 2:  
            if saida == 1:
                resultado = conv.BinarioParaDecimal(numero)
            elif saida == 3:
                resultado = conv.BinarioParaOctal(numero)
            elif saida == 4:
                resultado = conv.BinarioParaHexa(numero)
            else:
                resultado = numero

        elif entrada == 3:  
            if saida == 1:
                resultado = conv.OctalParaDecimal(numero)
            elif saida == 2:
                resultado = conv.OctalParaBinario(numero)
            elif saida == 4:
                resultado = conv.OctalParaHexa(numero)
            else:
                resultado = numero

        elif entrada == 4: 
            if saida == 1:
                resultado = conv.HexaParaDecimal(numero)
            elif saida == 2:
                resultado = conv.HexaParaBinario(numero)
            elif saida == 3:
                resultado = conv.HexaParaOctal(numero)
            else:
                resultado = numero

        print(f"\nResultado da conversão: {resultado}")


if __name__ == "__main__":
    main()
