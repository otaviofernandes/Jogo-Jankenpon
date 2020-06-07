from random import randint
from time import sleep
import datetime
import pygame
import os

#---------------------------------------------------------------
def musica(audio):
    aud = {1:'audio\m1.mp3', 2:'audio\m2.mp3', 3:'audio\m3.mp3',
           4:'audio\m4.mp3',5:'audio\m5.mp3',6:'audio\m6.mp3',
           7: 'audio\m7.mp3', 8: 'audio\m8.mp3'}
    pygame.mixer.music.load(aud[audio])
    pygame.mixer.music.play()
    return
#---------------------------------------------------------------
def pedra():
    print("    _______")
    print("---'   ____)")
    print("      (_____)")
    print("      (_____)")
    print("      (____)")
    print("---.__(___)")
    return
#---------------------------------------------------------------
def papel():
    print('    _.-._ ')
    print('   | | | |_')
    print('   | | | | |')
    print('_. | ´-._  |')
    print('\`\ __  `- .')
    print(' \ \   ´   |')
    print('  \.`     /')
    print('   |     |')
    return
#---------------------------------------------------------------
def tesoura():
    print(' .-.   _')
    print(' | |  / )')
    print(' | | / /')
    print(' | __ /_ ')
    print('/ __(-´ )')
    print('\  `(.-´)')
    print(' >._> -´')
    print('/\ /')
    return
#---------------------------------------------------------------
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return
#---------------------------------------------------------------
def cabecalho():
    cls()
    print('╔' + '═' * 78 + '╗')
    print('║ {:^76} ║'.format('P E D R A - P A P E L - T E S O U R A'))
    print('╚' + '═' * 78 + '╝')
    return
#---------------------------------------------------------------
def placar_game(game, win, lose, equal, vic, eq, lo):

    print('\n{:^38}'.format('R E S U L T A D O S'))
    print('╔' + '═' * 35 + '╗')
    print(f'   Total de partidas..: {game}')
    print(f'   Vitórias...........: {win} -> {vic:.1f}%')
    print(f'   Empates............: {equal} -> {eq:.1f}%')
    print(f'   Derrotas...........: {lose} -> {lo:.1f}%')
    print('╚' + '═' * 35 + '╝\n')
    print("─" * 80)
    return
#---------------------------------------------------------------
def escolha_player(player_choice, nome):
    if player_choice == '1':
        print('%s escolheu PEDRA!\n' % nome)
        pedra()
    elif player_choice == '2':
        print('%s escolheu PAPEL!\n' % nome)
        papel()
    elif player_choice == '3':
        print('%s escolheu TESOURA!\n' % nome)
        tesoura()
    return
#---------------------------------------------------------------
def escolha_npc(computer_choice):
        
    if computer_choice == '1':
        print('\nO computador escolheu PEDRA!\n')
        pedra()
    elif computer_choice == '2':
        print('\nO computador escolheu PAPEL!\n')
        papel()
    elif computer_choice == '3':
        print('\nO computador escolheu TESOURA!\n')
        tesoura()
    return
#---------------------------------------------------------------
def jan_ken_pon():
    musica(2)
    sleep(0.1)
    print('\n...JAN')
    sleep(0.7)
    print('......KEN')
    sleep(0.6)
    print('..........PON\n')
    sleep(0.1)
    return
#---------------------------------------------------------------
def nome_jogador():
    pygame.mixer.init()
    musica(8)
    cabecalho()
    nome = input('\nB E M - V I N D O!\nDigite seu nome ou tecle enter para continuar: ')
    if nome == '':
        nome = 'ANÔNIMO'
    else:
        nome = nome.upper()
    cls()
    return nome
#---------------------------------------------------------------
def jogar():
    nome = nome_jogador()
    game = 0
    win = 0
    lose = 0
    equal = 0
    vic = 0.001
    lo = 0.001
    eq = 0.001
    cont = 'S'
    while cont == 'S':
        pygame.mixer.init()
        musica(1)
        cabecalho()
        placar_game(game, win, lose, equal, vic, eq, lo)
        player_choice = str(input("Escolha Pedra(1), Papel(2) ou Tesoura(3):\n"))
        if (player_choice == '1') or (player_choice == '2') or (player_choice == '3'):
            jan_ken_pon()
            escolha_player(player_choice, nome)
            computer_choice = str(randint(1, 3))
            escolha_npc(computer_choice)
            sleep(1)
            if player_choice == '1' and computer_choice == '3':
                musica(3)
                print('\n%s GANHOU!\n'% nome)
                win = win + 1    
            elif player_choice == '1' and computer_choice == '2':
                musica(4)
                print('\n%s PERDEU!\n' %nome)
                lose = lose + 1
            elif player_choice == '1' and computer_choice == '1':
                musica(5)
                print('\nO jogo EMPATOU!\n')
                equal = equal + 1
            elif player_choice == '2' and computer_choice == '1':
                musica(3)
                print('\n%s GANHOU!\n'% nome)
                win = win + 1
            elif player_choice == '2' and computer_choice == '3':
                musica(4)
                print('\n%s PERDEU!\n' %nome)
                lose = lose + 1
            elif player_choice == '2' and computer_choice == '2':
                musica(5)
                print('\nO jogo EMPATOU!\n')
                equal = equal + 1
            elif player_choice == '3' and computer_choice == '2':
               musica(3)
               print('\n%s GANHOU!\n'% nome)
               win = win + 1
            elif player_choice == '3' and computer_choice == '1':
                musica(4)
                print('\n%s PERDEU!\n' %nome)
                lose = lose + 1 
            elif player_choice == '3' and computer_choice == '3':
                musica(5)
                print('\nO jogo EMPATOU!\n')
                equal = equal + 1
            game = game + 1
            vic = win / game * 100
            lo = lose / game * 100
            eq = equal / game * 100
            placar_game(game, win, lose, equal, vic, eq, lo)
            cont = input('\nJogar novamente? Aperte S (Sim) para continuar ou qualquer outra tecla para sair.\n')
            cont = cont.upper()     
            if cont != 'S':
                musica(6)
                print('\n      --- GAME OVER ---')
                sleep(3)
                cls()
                cria_txt()
                gravar_resultado(nome, game, win, lose, equal)          
        else:
            musica(6)
            print('\nVocê escolheu uma opção inválida!\n\n      --- GAME OVER ---')
            sleep(3)
            cls()
            cria_txt()
            gravar_resultado(nome, game, win, lose, equal)
            break
    return
#---------------------------------------------------------------
def gravar_resultado(nome, game, win, lose, equal):
    data = datetime.datetime.now()
    hoje = '{}/{}/{} - {}:{}'.format((data.day),(data.month),(data.year), (data.hour), (data.minute))
    arquivo = open('score\m.txt', 'a')
    registro = '{:^15}{:^25}{:^10}{:^10}{:^10}{:^10}\n'.format(hoje, nome, game, win, lose, equal)
    arquivo.write(registro)
    arquivo.close()
    return
#---------------------------------------------------------------
def cria_txt():
    try:
        arquivo = open('score\m.txt', 'r')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open('score\m.txt', 'w')
        arquivo.close()
    return
#---------------------------------------------------------------
def menu_principal():
    pygame.mixer.init()
    musica(7)
    cabecalho()
    print('\n{:^38}'.format('M E N U    P R I N C I P A L'))
    print('╔' + '═' * 35 + '╗')
    print(f'   (1) Nova partida..........:')
    print(f'   (2) Histórico de partidas.:')
    print(f'   (3) Sair do jogo..........:')
    print('╚' + '═' * 35 + '╝\n')
    return
#---------------------------------------------------------------
def mostrar_placar():
    pygame.mixer.init()
    musica(7)
    cria_txt()
    cabecalho()
    arquivo = open('score\m.txt', 'r')
    print('\n\n{:^80}\n{}'.format('H I S T Ó R I C O  D E  P A R T I D A S',('═'*80)))
    print('{:^15}{:^25}{:^10}{:^10}{:^10}{:^10}'.format('DATA', 'JOGADOR', 'PARTIDAS', 'VITÓRIAS', 'DERROTAS', 'EMPATES'))
    print('{}'.format('═'*80))
    print(arquivo.read())
    arquivo.close
    print('{}'.format('═'*80))
    print('\nDeseja limpar o histórico de partidas?')
    print('{}'.format('═'*40))
    print('(1) Para limpar todo o histórico...:')
    print('(2) Para voltar ao Menu Principal..:')
    print('{}\n'.format('═'*40))
    opcao = input('Escolha uma das opções 1 / 2: ')
    if opcao == '1':
        arquivo = open('score\m.txt', 'w')
        arquivo.close()
    return
#---------------------PROGRAMA PRINCIPAL------------------------
opcao = '1'
while opcao != '3':
    menu_principal()
    opcao = input('Escolha uma das opções 1 / 2 / 3: ')
    while opcao not in '123':
        print('Opção inválida!\n')
        opcao = input('Escolha uma das opções 1 / 2 / 3: ')
    if opcao == '1':
        jogar()
    elif opcao == '2':
        mostrar_placar()
    elif opcao == '3':
        pygame.mixer.init()
        cls()
        musica(6)
        sleep(3)
        break














