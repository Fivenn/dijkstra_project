def dijkstra(graph,startPoint,endPoint,visited=[],distances={},predecessors={}):
    
    # On verifie si les 2 points sont dans notre réseau
    if startPoint not in graph:
        print('Le point de départ n\'existe pas.')
    if endPoint not in graph:
        print('Le point d\'arrivé n\'existe pas.')  
    if startPoint != endPoint:
        # On commence en mettant le point de départ à 0
        if not visited: 
            distances[startPoint]=0
        # Puis nous visitons les points voisins pour calculer leurs distances 
        for neighbor in graph[startPoint] :
            if neighbor not in visited:
                newDistance = distances[startPoint] + graph[startPoint][neighbor]
                if newDistance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = newDistance
                    predecessors[neighbor] = startPoint
        # On marque les points voisins comme étant visités
        visited.append(startPoint)
        # Maintenant que les points voisins sont visités, on choisit le prochain point avec le poids le plus bas.

        unvisited={}   
        for p in graph:
            if p not in visited:
                unvisited[p] = distances.get(p,float('inf'))        
        dijkstra(graph,min(unvisited, key=unvisited.get),endPoint,visited,distances,predecessors)
    else :
        # Maintenant que tous les points dans le réseau sont visités, on obtient le chemin 
        path=[]
        pred=endPoint
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        path.reverse()
        print("Le chemin le plus court : {} avec une distance de {} ".format(path, distances[endPoint]))


    
startPoint = input('Point de départ : ').lower()
destinationPoint = input ('Point d\'arrivé : ').lower()
# Le réseau est donné sous la forme de "graph"
graph = {
    'a':{
        'b':2,
        'c':5
    },
    'b':{
        'e':2
    },
    'c':{
        'e':1,
        'b':2
    },
    'd':{
        'c':4,
        'b':1
    },
    'e':{
        'f':2,
        'd':4
    },
    'f':{
        'd':1
    }
}
dijkstra(graph,startPoint,destinationPoint)