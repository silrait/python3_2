import random


def imprime_apresentacao():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def selecionar_palavra(nome_arquivo='palavras.txt'):
    palavras = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    return palavras[random.randrange(0, len(palavras))]


def pedir_chute():
    chute = input('Digite uma letra: ').lower().strip()

    return chute


def exibir_resultado_jogo(informacoes_do_jogo):
    palavra_chute = ''.join(informacoes_do_jogo['lista_chute'])
    if (informacoes_do_jogo['tentativas'] == 0):
        print('Enforcou! A palavra era: {}'.format(informacoes_do_jogo['palavra_secreta']))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    elif (informacoes_do_jogo['palavra_secreta'] == palavra_chute):
        print('Parabéns vc acertou a palavra: {}'.format(palavra_chute))
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    print("Fim do jogo")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def exibir_resultado_rodada(informacoes_do_jogo):
    palavra_chute = ''.join(informacoes_do_jogo['lista_chute'])
    print('Tentativas restantes: {}'.format(informacoes_do_jogo['tentativas']))
    print('Palavra: {}'.format(palavra_chute))
    desenha_forca(7 - informacoes_do_jogo['tentativas'])


def valida_condicoes(informacoes_do_jogo):
    palavra_chute = ''.join(informacoes_do_jogo['lista_chute'])
    return informacoes_do_jogo['palavra_secreta'] != palavra_chute and informacoes_do_jogo['tentativas'] > 0


def valida_entrada(informacoes_do_jogo, chute):
    if (len(chute) == 1):
        informacoes_do_jogo['chute'] = chute
    else:
        raise ValueError('Digite uma, e somente uma letra!')

    return informacoes_do_jogo


def verifica_chute(informacoes_do_jogo):
    palavra_secreta = informacoes_do_jogo['palavra_secreta']
    chute = informacoes_do_jogo['chute']

    if (chute in palavra_secreta):
        for i in range(0, len(palavra_secreta)):
            if (palavra_secreta[i] == chute):
                informacoes_do_jogo['lista_chute'][i] = chute
    else:
        informacoes_do_jogo['tentativas'] -= 1


def jogar():
    imprime_apresentacao()

    informacoes_do_jogo = dict(palavra_secreta=selecionar_palavra('arquivo.txt'), tentativas=7)
    informacoes_do_jogo['lista_chute'] = ['_' for letra in informacoes_do_jogo['palavra_secreta']]

    while (valida_condicoes(informacoes_do_jogo)):
        exibir_resultado_rodada(informacoes_do_jogo)

        try:
            verifica_chute(valida_entrada(informacoes_do_jogo, pedir_chute()))
        except ValueError as erro:
            print(erro)
            continue

    exibir_resultado_jogo(informacoes_do_jogo)


if (__name__ == "__main__"):
    jogar()
