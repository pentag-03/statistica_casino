import random


def play_x2(bet, capital):
    for i in range(10):
        if capital - bet > 0:
            capital -= bet
            x = random.randint(0, 1)
            if x == 1:
                capital += bet * 2
    return (bet, capital)


persone_aggiornato = [
    {
        "name": "antonio",
        "capital": 1000,
        "bet": 10
    },
    {
        "name": "francesco",
        "capital": 1000,
        "bet": 10
    }
]


for i in persone_aggiornato:
    temp = play_x2(i["bet"], i["capital"])
    i["bet"] = temp[0]
    i["capital"] = temp[1]

print(persone_aggiornato)
