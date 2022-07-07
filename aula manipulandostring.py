# cada string tem um indice, que indica a posição da string

#       [012345678] Positivos
texto = 'Python s2'
#      -[987654321] Negativos

print(texto[2])  # vai mostrar a letra t que índice 2 do exemplo
print(texto[2:5])   # fatiamento de string
print(texto[:6])    # para começar da primeira string começa somente com :
print(texto[7:])    # se é para ir até o final da string termina com :
print(texto[:-1])   # negativo pode ser usado para tirar a última string
print(texto[:-4])   # negativo também pode ser usado para definir onde acaba a string, para fatiar a string
print(texto[0:6:2])  # nesse caso começa e vai até o 5 pulando de 2 em 2
print(texto[0::3])  # string completa pulando de 3 em 3
print(texto[0])
