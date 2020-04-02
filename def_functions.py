#função de pass line bet
def pass_line_bet(num_bet_plb):
    if soma_dos_dados == 7 or soma_dos_dados == 11:
        num_fichas += bet_plb
        print (num_fichas)
    elif soma_dos_dados in [2,3,12]:
        num_fichas -= bet_plt
        print (num_fichas)
    else:
        fase = "Point"
        dados_em_PLB = soma_dos_dados
    return num_fichas
#função de field
def field(num_bet_field):
    if soma_dos_dados in [3,4,9,10,11]:
        num_fichas += num_bet_field
        print (num_fichas)
    if soma_dos_dados == 2:
        num_fichas += (2*num_bet_field)
        print (num_fichas)
    elif soma_dos_dados == 12:
        num_fichas += (3*num_bet_field)
        print (num_fichas)
    else:
        num_fichas -= num_bet_field
        print (num_fichas)
    return num_fichas

#função de any craps
def any_craps(num_bet_any_craps):
    if soma_dos_dados in [2,3,12]:
        num_fichas += (num_bet_any_craps*7)
        print (num_fichas)
    else:
        num_fichas -= num_bet_any_craps
    return num_fichas

#função de twelve
def twelve(num_bet_twelve):
    if soma_dos_dados == 12:
        num_fichas += (num_bet_twelve*30)
    else:
        num_fichas -= num_bet_twelve
    return num_fichas
