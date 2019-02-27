def jogar():
    print('*********************************')
    print("** bem-vindo ao jogo de forca! **")
    print('*********************************')

    palavra_secreta = 'banana'
    tentativas = 5
    palavra_chute = '_' * len(palavra_secreta)

    print('palavra a ser adivinhada: {}, possui {} letras'.format(palavra_chute, len(palavra_chute)))

    while(palavra_chute != palavra_secreta and tentativas > 0):
        print('Letras acertadas: {}'.format(palavra_chute))

        lista_chute = list(palavra_chute)

        chute = input('Dê seu chute: ').lower().strip()

        if(chute in palavra_secreta):
            for i in range(0,len(palavra_secreta)):
                if(chute == palavra_secreta[i]):
                    lista_chute[i] = chute
        else:
          tentativas -= 1
        print('Você errou! Tentativas restantes: {}'.format(tentativas))

        palavra_chute = ''.join(lista_chute)

        if(palavra_chute == palavra_secreta):
            print('Você acertou a palavra {}'.format(palavra_chute))

    print('Fim do Jogo')


if(__name__ == '__main__'):
    jogar()
