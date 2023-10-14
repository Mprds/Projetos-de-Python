# Criar uma calculadora simples

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
# primeiro criei as variaveis que inserem os valores 

print('Qual operação você deseja fazer')
print('...1 - Soma')
print('...2 - Subtração')
print('...3 - Multiplicação')
print('...4 - Divisão')
# Apresento as operações a serem escolhidas

op =input('Digite o valor entre (1-4)')
if (op == '1'):
    print(num1,'+',num2,'=',num1+num2)
elif (op =='2'):
    print(num1,'-',num2,'=',num1-num2)
elif (op =='3'):
    print(num1,'*',num2,'=',num1*num2)
elif(op =='4'):
    print(num1,'/',num2,'=',num1/num2)
else:
    print('Valor incorreto')

