import names
import random
'''
il sentiment del giocatore sarà un parametro che va da 0 a 10
0 = pessimista
100 = ottimista
'''


header = ["name", "capital", "bet", "sentiment"]


random_data = []

for i in range(int(input("quante righe random vuoi?"))):
    random_data.append([])
    for head in header:
        if head == "name":
            'random name'
            random_data[i].append(names.get_full_name())
        if head == "capital":
            'random capital'
            random_data[i].append(int(1000))
        if head == "bet":
            'random bet'
            random_data[i].append(int(10))
        if head == "sentiment":
            'random sentiment'
            random_data[i].append(random.randint(0, 50))


for i in range(len(random_data)):
    print(random_data[i])


count_ludopatici = 0


def play(bet, capital, ripeti, n_vincenti, reward, sentiment):
    for i in range(ripeti):
        if sentiment >= random.randint(1, 100):
            bet *= 2
            count_ludopatici += 1
        if capital > bet:
            capital -= bet
            n_estratto = random.randint(0, 36)
            if n_estratto in n_vincenti:
                capital += bet * reward
                if random.randint(0, 3) == 1:
                    sentiment += 20
    return (bet, capital)


'''

se un giocatore vince il suo sentiment ha una probabilità di aumentare di 1/3 
il sentiment nel caso in cui aumenti avrà un aumento di 20 punti

in base al sentiment c'è una probabilità percentuale equivalente al valore numerico del sentiment di raddoppiare la puntata

cosa ci devo mettere

1) mi serve 1 if per determinare se il sentiment del giocatore dopo una vincita aumenta oppure no, la probabilità che aumenti è di 1/4
2) prevedere un if che aumenta la puntata in base al sentiment

'''
