from cria_baralho import cria_baralho
from Extrai_naipe import extrai_naipe
from empilha_carta import empilha
from extrair_valor import extrai_valor
from Possui_movimentos import possui_movimentos_possiveis
from movimenta_listas import lista_movimentos_possiveis 
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"





print('-------------------------------------------------------------------------------------')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.') 
print('')
print('Existem apenas dois movimentos possíveis:') 
print('')
print('1. Empilhar uma carta sobre a carta imediatamente anterior;') 
print('2. Empilhar uma carta sobre a terceira carta anterior.') 
print('')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: ')
print('')
print('1. As duas cartas possuem o mesmo valor ou') 
print('2. As duas cartas possuem o mesmo naipe.' )
print('')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.') 
print('')
print(input('Aperte [Enter] para iniciar o jogo...'))
print('-------------------------------------------------------------------------------------')
print('')



baralhon = cria_baralho() 
pm = possui_movimentos_possiveis(baralhon)
pm=True

while pm:
    for i in baralhon:
        for c in range(1,len(baralhon)+1):
            print (c,baralhon[c-1])
        pergunta1 = int(input('Qual carta voce quer?(digite um numero de 1 - {})  '.format(len(baralhon))))
        if pergunta1 <= 1 or pergunta1 > len(baralhon):
            print('Movimento Invalido')
            continue
        else:
            print('A carta selecionada é {}'.format(baralhon[pergunta1-1]))
            lmp=lista_movimentos_possiveis(baralhon, pergunta1-1)
            if lmp == [1, 3]:
                print('Você quer empilhar a carta {} em qual posicao? '.format(baralhon[pergunta1-1]))
                print(RED+('1. {}'.format(baralhon[pergunta1-2])+RESET))
                print(BLUE+('2. {}'.format(baralhon[pergunta1-4])+RESET))
                pergunta2 =input('Qual opção voce deseja? ')
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
    if len(baralhon) == 1:
        print('Você jogou de maneira elegante! Parabéns')
    else:
        print('Que pena, você jogou de maneira deselegante!')
    gn=input('Quer jogar novamente? (sim ou nao) ')
    if gn == 'sim':
        print('-----------------------------------------------------------------------------------------')
        baralhon = cria_baralho() 
        continue
    elif gn == 'nao':
        break
print('Obrigado por jogar!!!')
    
    
    



              

 

    


    
    







