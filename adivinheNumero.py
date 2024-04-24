import random

def gera_numero_aleatorio():
    return random.randint(1, 100)

def adivinhe_numero(tentativas, numeros):
    while tentativas > 0:
        tentativa = int(input("Digite um número: "))
        tentativas -= 1
        if tentativa < numero:
            print(f"Muito baixo! {tentativas} tentativas restantes.")
        elif tentativa > numero:
            print(f"Muito alto! {tentativas} tentativas restantes.")
        else:
            print(f"Parabéns! Você acertou.")
            return
    print("Você perdeu! O número era {numero}.")

numero = gera_numero_aleatorio()
print("Bem-vindo ao jogo de adivinhação!\nQuantas tentativas você quer para adivinhar o numero de 0 a 100?")
tentativas = int(input())
print("Pensei em um número de 0 a 100. Tente adivinhar dando seu palpite:\n")
adivinhe_numero(tentativas, numero)