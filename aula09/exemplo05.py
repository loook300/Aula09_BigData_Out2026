def soma(x,y) :
    r = x + y
    return r #retorna o resuldado para quem chamou 
    #print (r)


for i in range (3): 
    num1 = float(input ('Informe um numero: '))
    num2 = float(input ('Informe outro numero: '))
    resultado = soma (num1 , num2) #chamada da função 
    print(resultado)

    
