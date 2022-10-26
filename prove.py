import random


giocatori = [
    {
        "name": "antonio",
        "capital": 1000,
        "bet": 10
    },
    {
        "name": "nico",
        "capital": 1000,
        "bet": 10
    }
]

giochi = {
    "2x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18],
    "3x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "6x": [1, 2, 3, 4, 5, 6],
    "12x": [1, 2, 3],
    "36x": [1]
}

reward = {
    "2x": 2,
    "3x": 3,
    "6x": 6,
    "12x": 12,
    "36x": 36
}

selezione = input(
    "bro seleziona la modalità di gioco, puoi scegliere fra: 2x, 3x, 6x, 12x, 36x \n")


def play(bet, capital, ripeti, n_vincenti, reward):
    for i in range(ripeti):
        if capital > bet:
            capital -= bet
            n_estratto = random.randint(0, 36)
            if n_estratto in n_vincenti:
                capital += bet * reward
    return (bet, capital)


for giocatore in giocatori:
    temp = play(giocatore["bet"], giocatore["capital"],
                10, giochi[selezione], reward[selezione])
    giocatore["bet"] = temp[0]
    giocatore["capital"] = temp[1]

print(giocatori)
