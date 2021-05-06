def extrai_valor(string):
    valor=string[0:len(string)-1]
    return valor
def extrai_naipe(string):
    naipe=string[-1]
    return naipe    
def lista_movimentos_possiveis(lista, po):
    retorno=[]
    if po==0:
        return retorno 
    elif po>=1:
        vc3=extrai_valor(lista[po-3])
        nc3=extrai_naipe(lista[po-3])
        vca=extrai_valor(lista[po-1])
        nca=extrai_naipe(lista[po-1])
        vc=extrai_valor(lista[po])
        nc=extrai_naipe(lista[po])
        if vca==vc or nca==nc:
            retorno.append(1)
        if po>=3:
            if vc3==vc or nc3==nc:
                retorno.append(3)
    return retorno 