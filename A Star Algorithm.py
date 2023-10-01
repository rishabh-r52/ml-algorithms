def AstarAlg(startnode, stopnode):
    openset = set(startnode)
    closedset = set()
    g = {}
    parents = {}
    g[startnode] = 0
    parents[startnode] = startnode

    print(f"Startnode: {startnode}")
    print(f"Stopnode: {stopnode}")

    while len(openset) > 0:
        n = None
        for v in openset:
            if n is None or (g[v] + heuristic(v) < g[n] + heuristic(n)):
                n = v
        
        print(f"Current Node: {n}")

        if n == stopnode or Graphnodes[n] is None:
            pass
        else:
            for (m, weight) in getneighbours(n):
                if m not in openset and m not in closedset:
                    openset.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                    print(f"Added {m} to openset with g = {g[m]}")
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closedset:
                            closedset.remove(m)
                            openset.add(m)
                            print(f"Updated {m} in openset with g = {g[m]}")

        if n is None:
            print('Path does not exist!')
            return None
        
        if n == stopnode:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(startnode)
            path.reverse()
            print(f'\nPath found: {path}')
            return path
        
        openset.remove(n)
        closedset.add(n)

    print('Path does not exist!')
    return None

def getneighbours(v):
    if v in Graphnodes:
        return Graphnodes[v]
    else:
        return None

def heuristic(n):
    Hdist = {'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0 }
    return Hdist[n]

Graphnodes = {
    'S': [('A', 1), ('G', 10)], 
    'A': [('C', 1), ('B', 2)],
    'B': [('D', 5)],
    'C': [('D', 3), ('G', 4)],
    'D': [('G', 2)]
}

# Call the A* algorithm with trace
trace = AstarAlg('S', 'G')

# print(trace)