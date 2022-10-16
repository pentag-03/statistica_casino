
import csv
import names


header = ["name", "capital", "bet"]


random_data = []


for i in range(int(input("quante righe random vuoi?"))):
    random_data.append([])
    for head in header:
        if head == "name":
            # random name
            random_data[i].append(names.get_full_name())
        if head == "capital":
            # random capital
            random_data[i].append(1000)
        if head == "bet":
            # random bet
            random_data[i].append(10)

with open('persone.csv', 'w', encoding='UTF8', newline='') as file:
    # create the csv writer
    writer = csv.writer(file)

    # write header to the csv file
    writer.writerow(header)

    # write the rows to the csv file
    for i in range(len(random_data)):
        writer.writerow(random_data[i])
