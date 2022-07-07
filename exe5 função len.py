nome = input('Digite seu nome: ')
tamanho = len(nome)

# len é usado para saber quantos caracteres tem

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é médio')
else:
    print('Seu nome é grande')
