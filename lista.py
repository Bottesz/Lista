"""generálj 5 véletlenszámot
    [10,35) között

"""
import random 
def veletlen():
    list = []
    ''' listában azonos adatok legyenek '''
    i:int = 0
    while i < 5:
        szam = random.random()*(36-10)+10
        list.append(szam)
        i += 1 
    return list
    
    



listam=veletlen()

"""Írjuk ki egymás alá a lista elemeit"""
def lista_kiir(lista):
    for i in range(0,len(lista),1):
        print(f"A lista {i}. eleme: {lista[i]}")


lista_kiir(listam)



def lista_kiir2(lista):
    n:int = 0
    while n < len(lista):
        print(f"A lista {n}. eleme: {lista[n]}")
        n += 1

lista_kiir2(listam)
