# su 3 giocate alla roulette quanto può vincere un giocatore
# creo una funzione che in base a un valore randomico da una vincita o perdita

# miglioramenti
'''
1) implementare il sentiment del giocatore
2) statistica che rileva quanti sono in profit e quanti in perdita
3) dataframe che riporta tutto il percorso di scommesse dell'utente
4) cambia la parte dove si aggiunge initial capital e mettila appena generi i dati random, perchè è inutile tenerla
'''

import csv
import random
import names
'bug'


'function for double your bet'


def play_x2(bet, capital):
    for i in range(10):
        if capital > bet:
            capital -= bet
            x = random.randint(0, 1)
            if x == 1:
                capital += bet * 2
    return (bet, capital)


'function for 3x your bet'


def play_x3(bet, capital):
    for i in range(10):
        if capital > bet:
            capital -= bet
            x = random.randint(0, 2)
            if x == 1:
                capital += bet * 3
    return (bet, capital)


'function for 6x your bet'


def play_x6(bet, capital):
    for i in range(10):
        if capital > bet:
            capital -= bet
            x = random.randint(0, 5)
            if x == 1:
                capital += bet * 6
    return (bet, capital)


'function for 12x your bet'


def play_x12(bet, capital):
    for i in range(10):
        if capital > bet:
            capital -= bet
            x = random.randint(0, 11)
            if x == 1:
                capital += bet * 12
    return (bet, capital)


'function for 36x your bet'


def play_x36(bet, capital):
    for i in range(10):
        if capital >= bet:
            capital -= bet
            x = random.randint(0, 35)
            if x == 1:
                capital += bet * 36
    return (bet, capital)


header = ["name", "capital", "bet"]


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


with open('persone.csv', 'w', encoding='UTF8', newline='') as file:
    'create the csv writer'
    writer = csv.writer(file)

    'write header to the csv file'
    writer.writerow(header)

    'write the rows to the csv file'
    for i in range(len(random_data)):
        writer.writerow(random_data[i])

with open('persone.csv', 'r') as file:
    reader = csv.reader(file, delimiter=",")
    persone = {}
    matrice = []
    matrice_temporanea = []
    matrice_ordinata = []
    contatore = 0
    for row in reader:
        matrice.append(row)

'ordina gli elementi in una lista'
for i in range(len(matrice[0])):
    for element in matrice:
        matrice_temporanea.append(element[i])

'trasferisce gli elementi ordinati in una matrice'
for i in range(len(matrice[0])):
    matrice_ordinata.append([])
    for ii in range(len(matrice)):
        matrice_ordinata[i].append(matrice_temporanea[contatore])
        contatore += 1

'crea il dizionario con le key e le rimuove dalla matrice'
for lista in matrice_ordinata:
    persone.update({lista[0]: None})


'aggiunge al dizionario i value, e i value sono castati a integer'
for key in persone.keys():
    for lista in matrice_ordinata:
        if key == lista[0]:
            del lista[0]
            if key == "capital" or key == "bet":
                for i in range(len(lista)):
                    lista[i] = int(lista[i])
            persone[key] = lista


'cambia il formato del dizionario in una lista di dizionari'
persone_aggiornato = []
for i in range(len(persone['name'])):
    persone_aggiornato.append({})
    for key, value in persone.items():
        diz_temp = {key: value[i]}
        persone_aggiornato[i].update(diz_temp)


'qui viene salvato il punto di partenza dei giocatori, il nome e il capitale, in una lista di dizionari'
profit_perdenti = []
for persona in persone_aggiornato:
    temp_dict = {"name": persona["name"], "capital": persona["capital"]}

    profit_perdenti.append(temp_dict)


'trascrizione dei risultati in una lista di dizionari'
for giocatore in persone_aggiornato:
    temp = play_x36(giocatore["bet"], giocatore["capital"])
    giocatore["bet"] = temp[0]
    giocatore["capital"] = temp[1]


'aggiunge una roba inutile'

for giocatori in persone_aggiornato:
    for dati_giocatori in profit_perdenti:
        if giocatori["name"] == dati_giocatori["name"]:
            giocatori.update({"initial_capital": dati_giocatori["capital"]})


'controlla chi è in perdita e chi in profitto'
vincenti = 0
perdenti = 0

for giocatori in persone_aggiornato:
    if giocatori["initial_capital"] < giocatori["capital"]:
        vincenti += 1
    else:
        perdenti += 1


print("quelli in profit sono " + str(vincenti))
print("quelli in perdita sono " + str(perdenti))
