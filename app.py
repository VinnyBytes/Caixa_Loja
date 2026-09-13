# Programa de descontos progressivos
# Criado por VinnyBytes

import time
# bloco para entrada de dados
def ler_valor():
    while True:     # Loop para garantir que o usuário digite um valor válido
        try:
            valor = float(input("\nDigite o valor do gasto: R$ ").replace(",", ".")) # 
            if valor < 0:
                print("Valor inválido. Por favor, digite um valor positivo.") # caso o usuário digite um valor negativo.
                continue
            return valor
        except ValueError: # caso o usuário digite um valor que não seja um número.
            print("Entrada inválida. Por favor, digite apenas números.")

# bloco para calcular o desconto
def calcular_desconto(valor_gasto):
    if valor_gasto <= 200:
        porcentagem_desconto = 5
    elif valor_gasto <= 300:
        porcentagem_desconto = 10
    else:
        porcentagem_desconto = 15

    valor_desconto = valor_gasto * (porcentagem_desconto / 100) # O valor do desconto é calculado multiplicando o valor gasto pela porcentagem de desconto.
    valor_final = valor_gasto - valor_desconto

    return porcentagem_desconto, valor_desconto, valor_final # a função retorna a porcentagem de desconto, o valor do desconto e o valor final a pagar.

print("\nBem-vindo ao programa assistente de descontos progressivos!") # Mensagem de boas-vindas ao usuário.

while True: # Loop para permitir múltiplas consultas
    valor_gasto = ler_valor()
    porcentagem_desconto, valor_desconto, valor_final = calcular_desconto(valor_gasto)
    
# Dados de saída
    print("\nAGUARDE... Calculando desconto...")
    time.sleep(3)
    print(f"Parabéns! Você recebeu um desconto de {porcentagem_desconto}%!")
    time.sleep(2)
    print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
    time.sleep(2)
    print(f"Valor final a pagar: R$ {valor_final:.2f}")
    time.sleep(2)

    resposta = input("\nDeseja consultar outro valor? (s/n): ").strip().lower()
    time.sleep(2)
    if resposta != "s":
        print("\nObrigado por usar o programa assistente de descontos progressivos!")
        time.sleep(2)
        print("Programa encerrado.")
        break