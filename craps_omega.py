#projeto finalizado
import random
import list_of_functions as lf
num_fichas = 100
print('Bem vindo ao jogo de Craps!')
print('Este jogo de apostas consiste em acertar algum dos valores gerados pela soma de dois dados comuns.')
print('Você possui {0} fichas.'.format(num_fichas))
print('O jogo é composto de duas fases, Come Out e Point.')
fase = "Come Out"
while num_fichas > 0:
    res_jogador = input("Você quer iniciar o jogo? s/n ")
    while res_jogador == 's' and fase == "Come Out":
        while fase == "Come Out":
            if num_fichas<=0:
                print("Você foi forçado a sair do jogo por não ter mais fichas para apostar")
            dado1= random.randint(1, 6)
            dado2= random.randint(1, 6)
            soma_dos_dados= dado1 + dado2
            print (soma_dos_dados)
            print('Sua fase é: Come Out.')
            print('Você pode fazer quatro tipos de apostas: Pass Line Bet, Field, Any Craps ou Twelve.')

            pass_line_bet_sn = input('Deseja apostar algum valor em Pass Line Bet? Sim ou Não? ')
            if pass_line_bet_sn == 'Sim':
                num_bet_plb = int(input('Quanto deseja postar? '))
                        
            field_sn = input('Deseja apostar algum valor em Field? Sim ou Não? ')
            if field_sn == 'Sim':
                num_bet_field = int(input('Quanto deseja apostar? '))

            any_craps_sn = input('Deseja apostar algum valor em Any Craps? Sim ou Não? ')
            if any_craps_sn == 'Sim':
                 num_bet_any_craps = int(input('Quanto deseja apostar? '))

            twelve_sn = input('Deseja apostar algum valor em Twelve? Sim ou Não? ')
            if twelve_sn == 'Sim':
                num_bet_twelve = int(input('Quanto deseja apostar? '))

            print('Jogando os dados, valor sorteado é de {0} e {1}, e a soma dos valores deu {2}' .format(dado1, dado2, soma_dos_dados))
            dados_em_plb = dado1+dado2
            if pass_line_bet_sn == 'Sim':
                num_fichas, fase, dados_em_plb = lf.pass_line_bet(num_bet_plb,soma_dos_dados,num_fichas)
                print ("pass line bet")
            if field_sn == 'Sim':
                num_fichas = lf.field(num_bet_field,soma_dos_dados,num_fichas)
                print ("field")
            if any_craps_sn == 'Sim':
                num_fichas = lf.any_craps(num_bet_any_craps,soma_dos_dados,num_fichas)
                print ("any craps")
            if twelve_sn == 'Sim':
                num_fichas = lf.twelve(num_bet_twelve,soma_dos_dados,num_fichas)
                print ("twelve")
        while fase == "Point":
            if num_fichas<=0:
                print("Você foi forçado a sair do jogo por não ter mais fichas para apostar")
            dado1= random.randint(1, 6)
            dado2= random.randint(1, 6)
            soma_dos_dados= dado1 + dado2
            print('Sua fase é: Point.')
            print('Você pode fazer três tipos de apostas: Field, Any Craps ou Twelve.')
            print('Para sair desta fase, é necessário que a soma dos dados seja igual ao "Point" ou a 7')
            field_sn = input('Deseja apostar algum valor em Field? Sim ou Não? ')
            if field_sn == 'Sim':
                num_bet_field = int(input('Quanto deseja apostar? '))

            any_craps_sn = input('Deseja apostar algum valor em Any Craps? Sim ou Não? ')
            if any_craps_sn == 'Sim':
                num_bet_any_craps = int(input('Quanto deseja apostar? '))

            twelve_sn = input('Deseja apostar algum valor em Twelve? Sim ou Não? ')
            if twelve_sn == 'Sim':
                num_bet_twelve = int(input('Quanto deseja apostar? '))

            print('Jogando os dados, valor sorteado é de {0} e {1}, e a soma dos valores deu {2}' .format(dado1, dado2, soma_dos_dados))

            if field_sn == 'Sim':
                num_fichas = lf.field(num_bet_field,soma_dos_dados,num_fichas)
            if any_craps_sn == 'Sim':
                num_fichas = lf.any_craps(num_bet_any_craps,soma_dos_dados,num_fichas)
            if twelve_sn == 'Sim':
                num_fichas = lf.twelve(num_bet_twelve,soma_dos_dados,num_fichas)
            if soma_dos_dados == dados_em_plb or soma_dos_dados == 7:
                fase = "Come Out"
                if soma_dos_dados == dados_em_plb:
                    num_fichas += num_bet_plb
                    print ("Parabéns você ganhou! Agora sua balança é de: {0} fichas".format(num_fichas))
                elif soma_dos_dados == 7:
                    num_fichas -= num_bet_plb
                    print ("Oh não você perdeu! Agora sua balança é de: {0} fichas!".format(num_fichas))
    if res_jogador == 'n':
        print ("OK até a próxima!")
        print ("Você está saindo do jogo com {0} fichas!".format(num_fichas))
        break
if num_fichas <= 0:
    print("Você foi forçado a sair do jogo por não ter mais fichas para apostar")
