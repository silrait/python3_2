import random

def selecionar_palavra(nome_arquivo):
    palavras = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    
    return palavras[ random.randrange(0, len(palavras))]


def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    palavra_secreta = selecionar_palavra('arquivo.txt')
    palavra_chute = '_' * len(palavra_secreta)
    tentativas = 5
    
    while(palavra_secreta != palavra_chute and tentativas > 0):
        print('Tentativas restantes: {}'.format(tentativas))
        print('Palavra: {}'.format(palavra_chute))
        chute = input('Digite uma letra: ').lower().strip()
        if(len(chute) != 1):
            print('Digite uma, e somente uma letra!')
            continue
        
        lista_chute = list(palavra_chute)
        
        if(chute in palavra_secreta):
            for i in range(0,len(palavra_secreta)):
                if(palavra_secreta[i] == chute):
                    lista_chute[i] = chute
        else:
            tentativas -= 1
            
        palavra_chute = ''.join(lista_chute)
       
    if(tentativas == 0):
        print('Enforcou! A palavra era: {}'.format(palavra_secreta))
    elif(palavra_secreta == palavra_chute):
        print('Parabéns vc acertou a palavra: {}'.format(palavra_chute))
    
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()