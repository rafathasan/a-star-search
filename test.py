import csv
import astarsearch as astar
import sys

data = {}
heuristic = {}
start = goal = str()
with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter=' ')
    target = next(reader)
    start = target[0]
    goal = target[1]
    headers = next(reader)
    heuristic = {k:int(v) for k,v in zip(headers, next(reader))}
    for row,header,i in zip(reader,headers,range(len(headers))):
        data[header] =  {headers[i]:int(x) for x,i in zip(row,range(len(row))) if headers[i] != header and int(x) != -1 }

result = astar.search(data, heuristic, 'S', 'G')
print('cost: {}, path: {}'.format(result['cost'],result['path']))