def search(data, heuristic, start, goal):

    parent = {}
    cost = {start:0}
    visited = []
    level = {start:heuristic[start]}

    while True:
        node = min(level, key=level.get)
        level.pop(node, None)
        visited.append(node)

        if node is goal:
            break

        for k,v in data[node].items():
            if k in visited:
                if cost[k] <= v+heuristic[k]:
                    continue
            cost[k] = cost[node] + v
            level[k] = v + heuristic[k]
            parent[k] = node
    
    path = [goal]
    node = goal

    while True:
        path.append(parent[node])
        node = parent[node]
        if(node) is start:
            break
    path.reverse()


    return {'path': path, 'cost': cost[goal]}



