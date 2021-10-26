from random import choice

def jogar():
    print('*********************************')
    print('   Bem vindo ao jogo da forca!   ')
    print('*********************************')

    palavras = ['banana', 'morango', 'ovo', 'mosca', 'vermelho']
    palavra_secreta = choice(palavras).upper()
    tentativas = 5
    lista_palavra = list(len(palavra_secreta) * '_')
    ja_escolhidas = []

    def mostra_lista_palavra():
        for letra in lista_palavra:
            print(letra, end='')

    enforcou = acertou = False

    while not enforcou and not acertou:
        print(f'\nTentativas: {tentativas}')
        mostra_lista_palavra()
        while True:
            chute = input('\nQual letra? ').strip().upper()
            if chute.isalpha():
                break
            else:
                print('Por favor, digite uma letra.')
        
        if chute in ja_escolhidas:
            print(f'\nVocê ja escolheu a letra {chute}')
            continue
        else:
            ja_escolhidas.append(chute)

        if chute in palavra_secreta.upper():
            print('Encontrei a letra {}!'.format(chute))
            i=0
            for letra in palavra_secreta.upper():
                if letra == chute:
                    lista_palavra[i] = letra
                if not '_' in lista_palavra:
                    acertou = True
                    print('\nVocê venceu!')
                    print(f'A palavra era: {palavra_secreta}')
                    break
                i+=1
        else:
            print(f'A palavra não possui a letra {chute}..')
            tentativas -= 1
            if tentativas == 0:
                enforcou = True
                print('\nVocê perdeu..')
                print(f'A palavra era: {palavra_secreta}')
                break
            print(f'Restam {tentativas} tentativas.')

    print('Fim do jogo')

if __name__ == '__main__':
    jogar()
