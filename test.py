import csv

data = {}
heuristic = {}
with open("dataset.csv") as f:
    reader = csv.reader(f, delimiter=' ')
    headers = next(reader)
    nth = 0
    for row,header in zip(reader,headers):
        data[header] = row
        heuristic[header] = row[nth]
        nth+=1

print(data)

print(heuristic)