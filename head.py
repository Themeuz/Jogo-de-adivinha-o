from random import randint
secret = randint(1, 10)

print ("Seja bem vindo ao jogo da adivinhação!")
guess = 0
while guess != secret:
    g = input("Escolha um número: ")
    guess = int(g)
    if guess == secret:
        print("Você venceu!")
    else:
        if guess > secret:
            print("Muito alto!")
        else:
            print("Muito baixo!")
print("Jogo finalizado")