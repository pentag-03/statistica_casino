import pandas as pd
import csv

url = "nuovo.csv"
df = pd.read_csv(url)
df = df.iloc[:-1]
print(df)


'''
il problema è quasi risolto devi solamente trasformare df in un csv file ed eliminare il vecchio oppure aggiorni il nuovo
devi mettere +1 nel range in prove di prove dove si scrive il file csv
'''
with open('nuovissimo.csv', 'w', encoding='UTF8', newline='') as file:
    # create the csv writer
    writer = csv.writer(file)
    writer.writerows(df)
