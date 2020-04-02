import random
#Jogo n pergunta ao jogador se ele quer continuar jogando o jogo antes da nova rodada comecar
#O código não é eficiente
#Próxima iteração seria trocar a maioria dos 'if' e 'else' para uma função só.
num_fichas = 50

print('Bem vindo ao jogo de Craps! \n')
print('Este jogo de apostas consiste em acertar algum dos valores gerados pela soma de dois dados comuns. \n')
print('Você possui {0} fichas. \n'.format(num_fichas))
print('O jogo é composto de duas fases, Come Out e Point.')

#loop usado até o fim das fichas
while num_fichas >= 0 :
    fase = "Come Out"

#código que realiza a soma dos valores sorteados
    dado1= random.randint(1, 6)
    dado2= random.randint(1, 6)
    soma= dado1 + dado2

#código para início da fase come out
    if fase == "Come Out" and num_fichas >0:
        print('Sua fase é: Come Out. \n')
        print('Você pode fazer quatro tipos de apostas: \n 1-Twelve, onde se a soma dos dados for 12, o jogador ganha trinta vezes o valor que apostou, se não, perde. \n 2-Field, se a soma for 5, 6, 7 ou 8, o jogador perde, se for  3, 4, 9, 10, ou 11 o jogador ganha o valor que apostou, se for 2, ele recebe o dobro do valor que \n apostou, e se for 12, ele recebe 3 vezes o valor que apostou. \n 3-Any Craps,se a soma dos dados for 2, 3 ou 12 o jogador ganha sete vezes o que apostou, senão perde. \n 4-Pass Line Bet, se a soma dos dados for 7 ou 11 o jogador ganha o valor que apostou, se for  2, 3 ou 12, o jogador perde, mas se a soma der 4, 5, 6, 8, 9 ou 10, o \n jogador vai para a fase Point.')

        Q = input('Deseja apostar algum valor em Twelve? Sim ou Não? ')
        if Q == 'Sim':
            valorQ = int(input('Quanto deseja postar? '))
            
        W = input('Deseja apostar algum valor em Field? Sim ou Não? ')
        if W == 'Sim':
            valorW = int(input('Quanto deseja apostar? '))

        E = input('Deseja apostar algum valor em Any Craps? Sim ou Não? ')
        if E == 'Sim':
            valorE = int(input('Quanto deseja apostar? '))

        R = input('Deseja apostar algum valor em Pass Line Bet? Sim ou Não? ')
        if R == 'Sim':
            valorR = int(input('Quanto deseja apostar? '))

        print('Jogando os dados, valor sorteado é de {0} e {1}, e a soma dos valores deu {2}' .format(dado1, dado2, soma))

#código das apostas da fase come out
#Twelve
        if Q == 'Sim' and num_fichas > 0:
            print('\n Na sua aposta em Twelve: ')
            if soma == 12:
                num_fichas = num_fichas + 30 * valorQ
                print('Você ganhou, agora possui {0} fichas. ' .format(num_fichas))
            else: 
                num_fichas =  num_fichas - valorQ 
                print('Você perdeu, agora possui {0} fichas. ' .format(num_fichas))
#Field
        if W == 'Sim' and num_fichas > 0:
            print('\n Na sua aposta em Field: ')
            if soma == 5 or soma == 6 or soma == 7 or soma ==8:
                num_fichas = num_fichas - valorW
                print('Você perdeu, agora possui {0} fichas.' .format(num_fichas))
            if soma == 3 or soma == 4 or soma ==9 or soma == 10 or soma == 11:
                num_fichas = num_fichas + valorW
                print('Você ganhou, onde a soma dos dados deu algum dos valores seguintes: 3, 4, 9, 10 ou 11, agora possui {0} fichas.' .format(num_fichas))
            if soma == 2:
                num_fichas = num_fichas + 2* valorW
                print('Você ganhou, onde a soma dos dados foi 2, agora possui {0} fichas.' .format(num_fichas))
            if soma == 12:
                num_fichas = num_fichas + 3* valorW
                print('Você ganhou, onde a soma dos dados foi 12, agora possui {0} fichas.' .format(num_fichas))
#Any Craps
        if E == 'Sim' and num_fichas > 0:
            print('\n Na sua aposta em Any Craps: ')
            if soma == 2 or soma == 3 or soma == 12:
                num_fichas = num_fichas + valorE * 7
                print('Você ganhou, agora possui {0} fichas. ' .format(num_fichas))
            else:
                num_fichas = num_fichas - valorE
                print('Você perdeu, agora possui {0} fichas. ' .format(num_fichas))

#pass line bet
        if R == 'Sim' and num_fichas > 0:
            print('\n Na sua aposta em Pass Line Bet: ')
            if soma == 7 or soma == 11:
                num_fichas = num_fichas + valorR
                print('Você ganhou, agora possui {0} fichas. ' .format(num_fichas))
            if soma == 2 or soma == 3 or soma == 12: # craps
                num_fichas = num_fichas - valorR
                print('Você perdeu, agora possui {0} fichas. ' .format(num_fichas))
    #aqui passa para a fase point           
            else:                          
                print('Você passou para a fase Point! \n ')
                print('Nesta fase, você tem três opções de aposta: Field, Any Craps e Twelve. ')
#valores das apostas para a fase point
            W = input('Deseja apostar algum valor em Field? Sim ou Não? ')
            if W == 'Sim':
                valorW = int(input('Qual valor deseja apostar em Field? '))

            E = input('Deseja apostar algum valor em Any Craps? Sim ou Não? ')
            if E == 'Sim':
                valorE = int(input('Qual valor deseja apostar em Any Craps? '))

            Q = input('Deseja apostar algum valor em Twelve? Sim ou Não? ')
            if Q == 'Sim':
                valorQ = int(input('Qual valor deseja apostar em Twelve? '))
#Código das apostas na fase point
        dado_point1 = random.randint(1,6)
        dado_point2 = random.randint(1,6)
        soma_2 = dado_point1+dado_point2
#Twelve
        if Q == 'Sim' and num_fichas > 0:
            print('Na sua aposta em Twelve: ')
            if soma_2 == 12:
                num_fichas = num_fichas + 30 * valorQ
                print('Você ganhou, agora possui {0} fichas. ' .format(num_fichas))
            else: 
                num_fichas =  num_fichas - valorQ 
                print('Você perdeu, agora possui {0} fichas. ' .format(num_fichas))
#Field
        if W == 'Sim' and num_fichas > 0:
            print('\n Na sua aposta em Field: ')
            if soma_2 == 5 or soma_2 == 6 or soma_2 == 7 or soma_2 ==8:
                num_fichas = num_fichas - valorW
                print('Você perdeu, agora possui {0} fichas.' .format(num_fichas))
            if soma_2 == 3 or soma_2 == 4 or soma_2 ==9 or soma_2 == 10 or soma_2 == 11:
                num_fichas = num_fichas + valorW
                print('Você ganhou, onde a soma dos dados deu algum dos valores seguintes: 3, 4, 9, 10 ou 11, agora possui {0} fichas.' .format(num_fichas))
            if soma_2 == 2:
                num_fichas = num_fichas + 2* valorW
                print('Você ganhou, onde a soma dos dados deu 2, agora possui {0} fichas.' .format(num_fichas))
            if soma_2 == 12:
                num_fichas = num_fichas + 3* valorW
                print('Você ganhou, onde a soma dos dados deu 12, agora possui {0} fichas.' .format(num_fichas))

#Any Craps

        if E == 'Sim' and num_fichas > 0:
            print('\n Na sua aposta em Any Craps: ')
            if soma_2 == 2 or soma_2 == 3 or soma_2 == 12:
                num_fichas = num_fichas + valorE * 7
                print('Você ganhou, agora possui {0} fichas. ' .format(num_fichas))
            else:
                num_fichas = num_fichas - valorE
                print('Você perdeu, agora possui {0} fichas. ' .format(num_fichas))
#código da fase point
        if soma_2 == 7 and num_fichas > 0:
            num_fichas = num_fichas - valorR 
            print('Você perdeu sua aposta em Point, agora tem {0} fichas.' .format(num_fichas))
        elif soma_2 == soma and num_fichas > 0:
            num_fichas = num_fichas + valorR
            print('Você ganhou sua aposta em Point, agora tem {0} fichas.' .format(num_fichas))
        elif soma_2 != 7 and soma_2 != soma and num_fichas > 0:
            Tentativas = 1
            while soma_2 != soma and soma_2 != 7:
                print('Jogando os dados novamente.')
                x3 = random.randint (1, 6)
                x4 = random.randint (1, 6)
                soma_2 = x3 + x4
                Tentativas += 1
            print('Jogando os dados, os valores sorteados foi de {0} e {1}, e a soma foi de {3}.' .format(x3, x4, soma_2))