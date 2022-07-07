# formatações de valores com modificadores
# :s para formatar texto (string)
# :d para formatar int
# :f para formatar float
# :.(número)f para formatar float (quantidade de casas decimais)  EX-  :.2f
# :(caractere) (> ou < ^) (quantidade) (tipo - s, d ou f)
# exemplo
n = 1
print(f'{n:0>10}')

nd = 1976
print(f'{nd:0>10}')

# > esquerda       < direita      ^ centro

# colocar como float

nt = 2467
print(f'{nt:0>10.2f}')

# exemplo com string

nome = 'Isabelle'
print(f'{nome:0^50}')
