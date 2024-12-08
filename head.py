print ("Seja bem vindo ao jogo da adivinhação!")
g = input("Escolha o número: ")
guess = int(g)
if guess == 5:
    print("Você acertou!")
else:
    print("Você errou!")
print("Jogo finalizado")