import random

def jogar():
    erros = 7
    mensagem_inicial()
    palavra_secreta = ler_palavra()

    enforcou = False
    acertou = False

    tamanho = len(palavra_secreta)
    letras_acertadas = ['?' for letra in palavra_secreta]

    print(f'A palavra secrete tem {tamanho} letras, vamos la!\n')
    print (f'{letras_acertadas}\n')

    while(not enforcou and not acertou):
        enforcou, acertou = teste_do_chute(palavra_secreta, letras_acertadas, erros)

    if acertou:
        mensagem_acertou()
    else:
        mensagem_errou(palavra_secreta)


    print("Fim do jogo")

def mensagem_inicial():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def ler_palavra():
    with open('frutas.txt', 'r') as texto:
        palavras = []
        for palavra in texto:
            palavras.append(palavra.strip().lower())
        index = random.randrange(0, len(palavras))
    return palavras[index]

def chutes():
   letra = input ('Chute uma letra\n')
   return letra

def teste_do_chute(palvra, acertadas, erros):

    enforcou = False
    acertou = False
    index = []
    i = 0
    acertos = 0
    tamanho = len(palvra)
    while(not enforcou and not acertou):
        if acertos != tamanho:
        
            chute = chutes()

        for letra in palvra:
            if chute.lower().strip() == letra:
                acertos += 1
                index.append(i+1)
                acertadas[i] = letra
            i += 1
        print(acertadas)

        if chute.lower().strip() not in palvra:
            erros -= 1
            desenha_forca(erros)
            
        enforcou = erros == 0
        acertou = '?' not in acertadas
    return enforcou, acertou
    
def mensagem_acertou():
    print("Parabéns, você ganhou!")
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

def mensagem_errou(palavra):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra))
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

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
