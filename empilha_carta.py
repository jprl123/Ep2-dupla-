def empilha(lista, o, d):
    lista[d]=lista[o]
    del lista[o]
    return lista