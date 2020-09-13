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

        for subnode,tcost in data[node].items():
            if subnode in visited:
                if cost[subnode] <= tcost + heuristic[subnode]:
                    continue
            cost[subnode] = cost[node] + tcost
            level[subnode] = tcost + heuristic[subnode]
            parent[subnode] = node
    
    path = [goal]
    node = goal

    while True:
        path.append(parent[node])
        node = parent[node]
        if(node) is start:
            break
    path.reverse()


    return {'path': path, 'cost': cost[goal]}



