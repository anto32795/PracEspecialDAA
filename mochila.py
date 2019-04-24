

'''
Estrategia voraz: ir cogiendo objetos menos pesados hasta que llegemos al maximo de la mochila
'''

def mochila_optima(objetos_optimizar,peso):
    mochila = []
    while(sum(mochila) < peso):
        if objetos_optimizar == []:
            return mochila
        elem = min(objetos_optimizar)
        if sum(mochila) + elem > peso:
            return mochila
        mochila.append(elem)
        objetos_optimizar.remove(elem)

    return mochila

objetos = [4,8,3,1]
c = 9

print(mochila_optima(objetos,c))