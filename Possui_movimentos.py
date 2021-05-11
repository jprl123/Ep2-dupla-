def extrai_valor(string):
    valor=string[0:len(string)-1]
    return valor
def extrai_naipe(string):
    naipe=string[-1]
    return naipe    
def possui_movimentos_possiveis(lista):
    x = 0
    for po in lista:
        vc3=extrai_valor(lista[x-3])
        nc3=extrai_naipe(lista[x-3])
        vca=extrai_valor(lista[x-1])
        nca=extrai_naipe(lista[x-1])
        vc=extrai_valor(lista[x])
        nc=extrai_naipe(lista[x])
        if vca==vc or nca==nc:
            return True
        if vc3==vc or nc3==nc:
            return True
        x+=1   
    else:
        return False
