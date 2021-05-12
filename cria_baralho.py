import random

def cria_baralho():
    cartas=['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    baralho=[]
    for i in cartas:
        baralho.append('- {}♠'.format(i))
        baralho.append('- {}♥'.format(i))
        baralho.append('- {}♦'.format(i))
        baralho.append('- {}♣'.format(i))
    random.shuffle(baralho)
    return baralho

   