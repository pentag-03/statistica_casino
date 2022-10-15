# su 3 giocate alla roulette quanto può vincere un giocatore
# creo una funzione che in base a un valore randomico da una vincita o perdita

# miglioramenti
# implementare una mole di utenti molto più grossa tramite file json
# implementare molti più giochi
# implementare il sentiment del giocatore
# il for dentro la funzione play dovrebbe essere tolto


# bug
#

import random

'function for double your bet'


def play_x2(bet, capital):
    for i in range(10):
        if capital - bet > 0:
            capital -= bet
            x = random.randint(0, 1)
            if x == 1:
                capital += bet * 2
    return(bet, capital)


'function for 3x your bet'


def play_x3(bet, capital):
    for i in range(10):
        if capital - bet > -1:
            capital -= bet
            x = random.randint(0, 2)
            if x == 1:
                capital += bet * 3
    return(bet, capital)


'function for 6x your bet'


def play_x6(bet, capital):
    for i in range(10):
        if capital - bet > -1:
            capital -= bet
            x = random.randint(0, 5)
            if x == 1:
                capital += bet * 6
    return(bet, capital)


'function for 12x your bet'


def play_x12(bet, capital):
    for i in range(10):
        if capital - bet > -1:
            capital -= bet
            x = random.randint(0, 11)
            if x == 1:
                capital += bet * 12
    return(bet, capital)


'function for 36x your bet'


def play_x36(bet, capital):
    for i in range(10):
        if capital - bet > -1:
            capital -= bet
            x = random.randint(0, 35)
            if x == 1:
                capital += bet * 36
    return(bet, capital)


persone = [
    {
        "name": "antonio",
        "capital": 100,
        "bet": 10
    },
    {
        "name": "francesco",
        "capital": 100,
        "bet": 10
    },
    {
        "name": "tiziano",
        "capital": 100,
        "bet": 10
    },
    {
        "name": "marco",
        "capital": 100,
        "bet": 10
    }
]

'trascrizione dei risultati in una lista di dizionari'
for i in persone:
    temp = play_x2(i["bet"], i["capital"])
    i["bet"] = temp[0]
    i["capital"] = temp[1]


print(persone)
