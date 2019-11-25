def dijkstra(graph,startPoint,endPoint,visited=[],distances={},predecessors={}):
    # Est-ce que le point de départ et le point d'arrivé appartiennent au graphe ?
    if startPoint not in graph:
        raise Exception('Le point de départ n\'existe pas.')
    if endPoint not in graph:
        raise Exception('Le point d\'arrivé n\'existe pas.')
    if startPoint != endPoint:
        # On met le poids du premier point à 0
        if not visited: 
            distances[startPoint]=0
        # On visite les successeurs de ce point pour calculer la distance
        for neighbor in graph[startPoint] :
            if neighbor not in visited:
                newDistance = distances[startPoint] + graph[startPoint][neighbor]
                if newDistance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = newDistance
                    predecessors[neighbor] = startPoint
        # On marque le point de départ comme étant visités
        visited.append(startPoint)
        unvisited={} 
         # On regarde chaque point du graphe et on marque ceux qui ne sont pas visités 
        for p in graph:
            if p not in visited:
                unvisited[p] = distances.get(p,float('inf'))
        # Fonction récursive permettant de travailler sur un graphe de taille plus petite ne comportant pas le point sélectionné       
        dijkstra(graph,min(unvisited, key=unvisited.get),endPoint,visited,distances,predecessors)
    else :
        # Une fois tout les points visités, on liste le meilleur chemin de routage
        path=[]
        pred=endPoint
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        path.reverse()
        print("Le chemin le plus court : {} avec une distance de {} ".format(path, distances[endPoint]))

startPoint = input('Point de départ : ').lower()
destinationPoint = input ('Point d\'arrivé : ').lower()
# Le graphe est sous la forme d'un dictionnaire comportant les points du graphes comportant eux-même un dictionnaire de leur successeurs avec leur poids
graph = {
    '1':{
        '2':10,
        '4': 30,
        '5':100
    },
    '2':{
        '3':50
    },
    '3':{
        '5':10,
    },
    '4':{
        '3':20,
        '5':60
    },
    '5':{
        # Pas de successeurs
    }
}
dijkstra(graph,startPoint,destinationPoint)