import random # importando a biblioteca random

health = 50 # atribuindo o valor de vida inicial da personagem

difficulty = 1 # o número representa a dificuldade do jogo

potion_health = int(random.randint (25,50) / difficulty) #quanto maior a dificuldade menor a quantidade de vida recupera

health = health + potion_health

print (health) # mostra o novo valor da vida