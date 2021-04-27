'''def cria_baralho():
    valores = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    lista = []
    for i in valores:
        baralho = [(valores)'♠', '(valores[i])♥','(valores[i])♣', '(valores[i])♦']
        lista.append([baralho])
    return lista

print(cria_baralho())'''


def cria_baralho():
    baralho = []
    valores = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']
    naipe=['♠', '♥', '♦', '♣','♠', '♥', '♦', '♣','♠', '♥', '♦', '♣','♠', '♥', '♦', '♣','♠', '♥', '♦', '♣','♠', '♥', '♦', '♣','♠', '♥', '♦', '♣','♠', '♥', '♦', '♣']
    i = 0
    juntar = 0
    while i < len(naipe):
        juntar = '{0} {1}'.format(valores[i], naipe[i])
        baralho.append(juntar)
        i +=1
    return baralho

print(cria_baralho())

    