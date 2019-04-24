'''
Algoritmo voraz:
Seleccionar Ci mas pequeño e ir montandolo de manera que
Fi sea cercano al siguiente Ci
sort(lista)
'''
import math

def actividades(lista_inicio,lista_fin):
    longitud = len(lista_inicio)
    tmp_ini = 0
    tmp_fin = 0
    lista_rtn = []
    sorted(lista_inicio)
    sorted(lista_fin)

    '''for j in lista_inicio:
        if j <=tmp_fin:
            tmp_ini = min(lista_inicio)
            for i in lista_fin:
                if i > tmp_ini:
                    tmp_fin = i
                    lista_fin.remove(i)
            lista_insertar[tmp_ini,tmp_fin]
            lista_rtn.append(lista_insertar)
            lista_inicio.remove(tmp_ini)
            lista_fin.remove(tmp_fin)'''
    for i in range(0,len(lista_inicio)):
        if lista_inicio[i]>=tmp_fin:
            lista_insertar = [lista_inicio[i],lista_fin[i]]
            tmp_fin = lista_fin[i]
            lista_rtn.append(lista_insertar)
    return lista_rtn

###############################
#   PROGRAMA PRINCIPAL  ####

ini = [1,4,5,8,13]
fin = [3,6,14,20,26]

print(actividades(ini,fin))

