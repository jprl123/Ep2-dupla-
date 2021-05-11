from cria_baralho import cria_baralho
from Extrai_naipe import extrai_naipe
from empilha_carta import empilha
from extrair_valor import extrai_valor
from Possui_movimentos import possui_movimentos_possiveis
from movimenta_listas import lista_movimentos_possiveis 




print('-------------------------------------------------------------------------------------')
baralhon = cria_baralho() #criando baralho
pm = possui_movimentos_possiveis(baralhon)
pm=True
while pm:
    for i in baralhon:
        for c in range(1,len(baralhon)+1):
            print (c,baralhon[c-1])
        pergunta1 = int(input('Qual carta voce quer?(digite um numero de 1 - {})  '.format(len(baralhon))))
        if pergunta1 <= 1 or pergunta1 > len(baralhon):
            print('movimento invalido')
        else:
            print('A carta selecionada é {}'.format(baralhon[pergunta1-1]))
            lmp=lista_movimentos_possiveis(baralhon, pergunta1-1)
            if lmp == [1, 3]:
                print('Você quer empilhar a carta {} em qual posicao? '.format(baralhon[pergunta1-1]))
                print('1. {}'.format(baralhon[pergunta1-2]))
                print('2. {}'.format(baralhon[pergunta1-4]))
                pergunta2 =input('Qual opção voce deseja vossa excelencia?')
                if pergunta2 != 1 or pergunta2 !=2:
                    print('opção invalida')
                if pergunta2 == '1':
                    empilha(baralhon, pergunta1-1, pergunta1-2)
                elif pergunta2 == '2':
                    empilha(baralhon, pergunta1-1, pergunta1-4)
            elif lmp == [1]:
                    empilha(baralhon, pergunta1-1, pergunta1-2)
            elif lmp == [3]:
                    empilha(baralhon,pergunta1-1, pergunta1-4)
            else:
                print('A carta selecionada {} não pode ser movida, escolha novamente'.format(baralhon[pergunta1-1]))
            pm = possui_movimentos_possiveis(baralhon)
    if pm ==False:
        if c==0:
            gn=input('Você jogou de maneira elegante! Quer jogar novamente? (sim ou nao) ')
            if gn=='nao':
                print('Acabou')
                pm=False
            elif gn == 'sim':
                pm=True
        else:
            jn=input('Você jogou de maneira deselegante! Quer tentar novamente? (sim ou nao)   ')
            if jn=='nao':
                print('Acabou')
                pm=False
            elif jn == 'sim':
                pm=True



              

 

    


    
    







