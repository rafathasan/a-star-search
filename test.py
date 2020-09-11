import csv

data = {}
heuristic = {}
with open("dataset.csv") as f:
    reader = csv.reader(f, delimiter=' ')
    headers = next(reader)
    nth = 0
    for row,header in zip(reader,headers):
        data[header] = [int(x) for x in row]
        heuristic[header] = int(row[nth])
        nth+=1

assert type(data['A'][0]) == int, "dataset value expected datatype: int, given: "+type(data['A'][0]).__name__
assert type(heuristic['A']) == int, "heuristic value expected datatype: int, given: "+type(heuristic['A']).__name__