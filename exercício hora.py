hora = input('Digite a hora: ')

if hora.isdigit():
    hora = int(hora)

    if hora < 0 or hora > 23:
        print('Por favor digite um horário de 0 a 23')
    else:
        if hora <= 11:
            print('Bom dia')
        elif hora <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Por favor digite um horário de 0 a 23')
