from random import randint
#começo do projeto
fase = "Come Out"
while num_fichas>0:
    ganhou = ("Parabéns você ganhou! Agora sua balança é de: " + num_fichas + "fichas")
    perdeu = ("Oh não você perdeu! Agora sua balança é de: " + num_fichas + " fichas!")
    if fase == "Come Out": #Programa todas as possibilidades para a fase Come Out
        print ("Você está na fase de " + fase)
        escolha = input("O que você deseja fazer (jogar/sair)? ") #jogador deve decidir toda rodada se ele vai participar ou sair do jogo
        if escolha == "sair":
            print ("Ok até a próxima!")
        else: #procurar outro jeito de escrever os tipos de apostas
            ganhou = ("Parabéns você ganhou! Agora sua balança é de: " + num_fichas + "fichas")
            perdeu = ("Oh não você perdeu! Agora sua balança é de: " + num_fichas + " fichas!")
            num_fichas_apostadas = int(input("Qual a quantidade que desejas apostar? "))
            if num_fichas_apostadas < num_fichas:
                print("Você não tem fichas suficientes para realizar esta aposta!")
            tipo_aposta = input("Digite o(s) tipos de aposta(s) que desejas: \n Pass Line Bet, Field, Any Craps ou Twelve?\n(Escreve utilizando letras maiúsculas, espaços e de forma respectiva) ")
            soma_prevista = int(input("Digite o valor da soma dos dois dados: "))
            cubo1 = randint(1,6)
            cubo2 = randint(1,6)
            soma_real = cubo1+cubo2
            if tipo_aposta == "Pass Line Bet":
                if soma_real == 7 or 11 and soma_prevista == soma_real:
                    num_fichas = num_fichas + num_fichas_apostadas
                    print(ganhou)
                elif soma_real ==2 or 3 or 12 and soma_prevista == soma_real:
                    num_fichas -= num_fichas_apostadas
                    print(perdeu)
                else:
                    print("Vamos para a fase de POINT")
                    fase = "Point"
            if tipo_aposta == "Field":
                if soma_real == 5 or 6 or 7 or 8 and soma_prevista == soma_real:
                    num_fichas -= num_fichas_apostadas
                    print(perdeu)
                if soma_real == 3 or 4 or 9 or 10 or 11 and soma_prevista == soma_real:
                    num_fichas += num_fichas_apostadas
                    print(ganhou)
                elif soma_real == 2 and soma_prevista == soma_real:
                    num_fichas += (2*num_fichas_apostadas)
                    print(ganhou)
                else:
                    num_fichas += (3*num_fichas_apostadas)
                    print(ganhou)
            if tipo_aposta == "Any Craps":
                if soma_real == 2 or 3 or 12 and soma_prevista == soma_real:
                    num_fichas += (7*num_fichas_apostadas)
                    print(ganhou)
                else:
                    num_fichas -= num_fichas_apostadas
                    print(perdeu)
            if tipo_aposta == "Twelve":
                if soma_real == 12 and soma_prevista == soma_real:
                    num_fichas += (30*num_fichas_apostadas)
                    print(ganhou)
                else:
                    num_fichas -= num_fichas_apostadas
                    print(perdeu)
    elif fase == "Point":
        
if num_fichas<=0: #esse vai ser o fim do código
        print ("Que pena você está sem fichas para apostar!")
        

        