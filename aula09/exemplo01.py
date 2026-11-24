produto1 = {} # dicionario vazio 

produto = {
    'nome': 'Notebook',
    'preco': 3500.80,
    'marca': 'lenovo',

}
# type(produto)
print(produto) #todas as chaves e valores


print(produto['nome'])#chave nome 
print(produto['preco'])#chave preco

#Alterando o valor
produto ['marca'] = "positivo"
print(produto['marca']) 

#adicionando CHaves
produto['tela'] = '18'
print(produto)

# Deletando um chave 
del produto ['marca']
print(produto)

print(produto.keys()) #chaves
print(produto.values()) # Valore
print(produto.items()) 
