def dobro(x):
    r = x *2 
    return r


def triplo(x):
    r = x *3 
    return r

def quadrado(x):
    r = x * x
    return r

num = float(input ('Informe um numero: '))
resultado_dobro = dobro (num)
resultado_tri = triplo (num)
resultado_qua = quadrado (num)


print (f'\nO dobro é {resultado_dobro}')
print (f'O tripulo é {resultado_tri}')
print (f'O quadrado é {resultado_qua}')

