listas = []

for i in range (3):
    print (f'\n Contatos {i+1}')
    lista= {}

    lista['nome'] = input ('Informe o nome completo: ')
    lista['telefone'] = int (input ('Informe o telefone: '))
    lista['email'] = (input ('Informe o e-mail: '))
    
    listas.append(lista)

#print (listas)

for elemento in listas: 
  
    print (f'\nNome :  {elemento ['nome']}')
    print (f'telefone :  {elemento ['telefone']}')
    print (f'E-mail :  {elemento ['email']}')

