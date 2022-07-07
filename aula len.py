# função len mostra quantos caracteres tem na string, não serve para float, int e bool
# o que é retornado da função len é int

usuario = input('Digite seu usuário: ')
caracteres = len(usuario)

print(usuario, caracteres, type(caracteres))

if caracteres < 6:
    print('Digite pelo menos 6 caracteres')
else:
    print('Digitou mais que 6 caracteres')

# exemplo dois = calcular a quantidade da soma de caracteres de duas string

string1 = input("Digite seu nome: ")
string2 = input("Digite seu sobrenome: ")

print(f'A quanridade total de caracteres digitados foi {len(string1) + len(string2)}')
