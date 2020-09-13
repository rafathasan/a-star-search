import csv
import astarsearch as astar

data = {}
heuristic = {}
with open("dataset.csv") as f:
    reader = csv.reader(f, delimiter=' ')
    headers = next(reader)
    for row,header,i in zip(reader,headers,range(len(headers))):
        data[header] =  {headers[i]:int(x) for x,i in zip(row,range(len(row))) if headers[i] != header and int(x) != -1 }
        heuristic[header] = int(row[i])

result = astar.search(data, heuristic, 'S', 'G')
print('cost: {}, path: {}'.format(result['cost'],result['path']))