p1 = "Por que o peixe não usa computador? \nR.: Porque tem medo do mouse."

p2 = "O que a impressora falou para a folha? \nR.: Esse trabalho é meu, você está só passando por aqui."

p3 = "O que aconteceu com o pato que botou um ovo quadrado? \nR.: Ele teve uma crise existencial."

p4 = "Por que o esqueleto não brigou com ninguém? \nR.: Porque ele não tem estômago para isso."

p5 = "Qual é o contrário de volátil? \nR.: Cadeira."

p6 = "O que um canibal vegetariano come? \nR.: Palhaçadas."

p7 = "Qual é o maior palhaço do mundo? \nR.: Você."

p8 = "Qual é o café mais perigoso do mundo? \nR.: O ex-presso."

p9 = "O que o advogado do frango disse ao juiz? \nR.: Que ele não foi o culpado, pois estava apenas fazendo o seu trabalho."

p10 = "O que uma árvore falou para outra? \nR.: Que madeira boa."

p11 = "O que um poste disse para o outro? \nR.: Você é de luz."

p12 = "Por que o elefante não pega fogo? \nR.: Porque ele já é cinza."

p13 = "Qual é o café mais perigoso do mundo? \nR.: O ex-presso."

p14 = "Por que o esqueleto não brigou com ninguém? \nR.: Porque ele não tem estômago para isso."

p15 = "O que o pato disse para a pata? \nR.: Vem Quá!"

p16 = "O que um canibal vegetariano come? \nR.: Palhaçadas."

p17 = (
    'Por que o morango foi ao médico? \nR.: Porque estava se sentindo um pouco "azedo".'
)

p18 = "O que a impressora falou para a folha? \nR.: Esse trabalho é meu, você está só passando por aqui."

p19 = "Qual é o contrário de volátil? \nR.: Cadeira."

p20 = "O que o nariz falou para o dedo? \nR.: Você me cheira?"

p21 = "O que a mão esquerda disse para a mão direita? \nR.: Nada, elas apenas deram um aperto de mão."

p22 = "O que uma parede falou para a outra? \nR.: Eu te encontro no canto."

p23 = "O que o tomate disse para o ketchup? \nR.: Ketchup, estamos a pé!"

p24 = 'Por que o relógio foi tocar na igreja? \nR.: Porque queria ser um "tic"-toque.'

p25 = "O que a escova de dente disse para o tubo de creme dental? \nR.: Mal posso esperar para trabalharmos juntos novamente."

p26 = "O que o zero disse para o oito? \nR.: Que cinto maneiro você está usando!"

p27 = "Por que o peixe não usa computador? \nR.: Porque tem medo do mouse."

p28 = "O que aconteceu com o pato que botou um ovo quadrado? \nR.: Ele teve uma crise existencial."

p29 = "Qual é o café mais perigoso do mundo? \nR.: O ex-presso."

p30 = "O que o advogado do frango disse ao juiz? \nR.: Que ele não foi o culpado, pois estava apenas fazendo o seu trabalho."

p31 = "Qual é a fruta que anda de trem? \nR.: O Kiwiiiiii"

piadas = []

for contador in range(1, 32):
    piada = globals()["p" + str(contador)]
    piadas.append(piada)


def get_piadas():
    return piadas
