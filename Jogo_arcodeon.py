from cria_baralho import cria_baralho
from Extrai_naipe import extrai_naipe
from empilha_carta import empilha
from extrair_valor import extrai_valor
from Possui_movimentos import possui_movimentos_possiveis
from movimenta_listas import lista_movimentos_possiveis 
baralhon = cria_baralho() #criando baralho
pm = possui_movimentos_possiveis(baralhon)
pm=True
while pm:
    pergunta1 = int(input('Qual carta voce quer ?(digite um numero de 1 - 52)  '))
    carta=baralhon[pergunta1 - 1]
    ali= int(pergunta1)
    if pergunta1 <= 1 or pergunta1 > 52:
        print('movimento invalido')
    lmp=lista_movimentos_possiveis(baralhon, ali)
    if lmp == [1, 3]:
        pergunta2=input('Você quer empilhar 1 ou 3?')
        if pergunta2 == '1':
            empilha(baralhon, baralhon[pergunta1], baralhon[pergunta1-1])
        elif pergunta2 == '3':
            empilha(baralhon, baralhon[pergunta1], baralhon[pergunta1-3])
    elif lmp == [1]:
        empilha(baralhon, baralhon[pergunta1], baralhon[pergunta1-1])
    elif lmp == [3]:
        empilha(baralhon, baralhon[pergunta1], baralhon[pergunta1-3])



    


    
    







