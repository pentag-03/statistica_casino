import random


def play_x2(bet, capital):
    for i in range(10):
        if capital - bet > 0:
            capital -= bet
            x = random.randint(0, 1)
            if x == 1:
                capital += bet * 2
    return (bet, capital)


persone = {
    'name': ['John', 'Marianne', 'Karen', 'antonino'],
    'capital': [1000, 1000, 1000, 10000],
    'bet': [10, 10, 10, 10]
}

persone_aggiornato = []
for i in range(len(persone['name'])):
    persone_aggiornato.append({})
    for key, value in persone.items():
        diz_temp = {key: value[i]}
        persone_aggiornato[i].update(diz_temp)

print(persone_aggiornato)

for i in persone_aggiornato:
    temp = play_x2(i["bet"], i["capital"])
    i["bet"] = temp[0]
    i["capital"] = temp[1]

print(persone_aggiornato)
