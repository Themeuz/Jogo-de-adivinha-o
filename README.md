# Jogo de advinhação
Um exercício da faculdade que se resume em escolher um número que o programa esteja disposto a passar.

### Versão 1.

``print ("Seja bem vindo ao jogo da adivinhação!")
g = input("Escolha o número: ")
guess = int(g)
if guess == 5:
    print("Você acertou!")
else:
    print("Você errou!")
print("Jogo finalizado")``


### Versão definitiva 2.

``from random import randint
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
print("Jogo finalizado")``

## Explicação:

A versão definitiva leva uma sequência de número de 1 a 10 que o próprio programa escolhe de maneira aleatória e imparcial, você só finaliza o programa quando acertar o número deixando mais dinâmico e mais próximo de um vídeo-game de verdade!