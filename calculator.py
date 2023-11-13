def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4 and num2 != 0:  # Verifica se o divisor não é zero
        resultado = num1 / num2
    else:
        resultado = 0  # Operação inválida ou divisão por zero
    
    return resultado

# Exemplo de uso:
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = int(input("Escolha a operação (1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão): "))

resultado_calculadora = calculadora(numero1, numero2, operacao)

print("Resultado:", resultado_calculadora)
