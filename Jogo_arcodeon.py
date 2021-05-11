import cria_baralho
import Extrai_naipe
import empilha_carta
import extrair_valor
import Possui_movimentos
import movimenta_listas 

baralho = cria_baralho() #criando baralho

pm = Possui_movimentos(baralho)

while pm:
    pergunta1 = int(input('Qual carta voce quer ?(digite um numero de 1 - 52'))
    if pergunta1 <= 0 or pergunta1 > 52 or pergunta1 == 1:
        print('movimento invalido')
        return pergunta1
    


    
    







