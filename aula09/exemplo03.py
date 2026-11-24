#titulo autor ano de publicação genero e numero de paginas 

lista_catalogo = []

for i in range(3):
    print (f'\n Livro {i+1}')

    livro ={}

    livro['titulo'] = input ('Informe o nome: ')
    livro['autor'] = input ('Informe o autor: ')
    livro['ano'] =int  (input ('Informe o ano de publicaçao: '))
    livro['genero'] = input ('Informe o genero: ')
    livro['paginas'] = int (input ('Informe o numero de paginas: '))

    lista_catalogo.append(livro)

#print (lista_catalogo)

for elemento in lista_catalogo: # 3 vezes 
    #print(elemento)
    if elemento['ano'] >= 2000 :
        print (f'Nome :  {elemento ['titulo']}')
        print (f'Ano :  {elemento ['ano']}')

