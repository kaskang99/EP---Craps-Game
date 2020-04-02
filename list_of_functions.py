def ganhou(num_fichas):
    ganhou = ("Parabéns você ganhou! Agora sua balança é de: {0} fichas".format(num_fichas))
    return ganhou
def perdeu(num_fichas):
    perdeu = ("Oh não você perdeu! Agora sua balança é de: {0} fichas!".format(num_fichas))
    return perdeu
#função de pass line bet
def pass_line_bet(num_bet_plb,soma_dos_dados,num_fichas):
    fase = "Come Out"
    dados_em_plb = 0
    if soma_dos_dados == 7 or soma_dos_dados == 11:
        num_fichas += num_bet_plb
        print (ganhou(num_fichas))
    elif soma_dos_dados in [2,3,12]:
        num_fichas -= num_bet_plb
        print (perdeu(num_fichas))
    else:
        fase = "Point"
        dados_em_plb = soma_dos_dados
        print ("Como a soma dos números está entre 4, 5, 6, 8, 9, 10, e 11, a fase será mudada para Point")
        return num_fichas, fase, dados_em_plb
    return num_fichas, fase, dados_em_plb
#função de field
def field(num_bet_field,soma_dos_dados,num_fichas):
    if soma_dos_dados in [3,4,9,10,11]:
        num_fichas += num_bet_field
        print (ganhou(num_fichas))
    if soma_dos_dados == 2:
        num_fichas += (2*num_bet_field)
        print (ganhou(num_fichas))
    elif soma_dos_dados == 12:
        num_fichas += (3*num_bet_field)
        print (ganhou(num_fichas))
    else:
        num_fichas -= num_bet_field
        print (perdeu(num_fichas))
    return num_fichas
#função de any craps
def any_craps(num_bet_any_craps,soma_dos_dados,num_fichas):
    if soma_dos_dados in [2,3,12]:
        num_fichas += (num_bet_any_craps*7)
        print (ganhou(num_fichas))
    else:
        num_fichas -= num_bet_any_craps
        print (perdeu(num_fichas))
    return num_fichas
#função de twelve
def twelve(num_bet_twelve,soma_dos_dados,num_fichas):
    if soma_dos_dados == 12:
        num_fichas += (num_bet_twelve*30)
        print (ganhou(num_fichas))
    else:
        num_fichas -= num_bet_twelve
        print (perdeu(num_fichas))
    return num_fichas
