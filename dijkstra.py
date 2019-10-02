from queue import *
def dijkstra(G, depart, arrivee):
    file_priorite = PriorityQueue()
    file_priorite.insert(depart, 0)
    dict_distance_min = {depart: 0}
    dict_predecesseur  = {} # Dictionnaire contenant le meilleur noeuf predecesseur pour le plus court chemin
    noeuds_visites = set()
    while True:
        entree = file_priorite.pop()
        if entree is None:
            break
        distance, noeud = entree
        if noeud not in noeuds_visites:
            noeuds_visites.add(noeud)
            if noeud == arrivee:
                break
            for successeur, longueur_arc in arcs_sortants(G, noeud):
                nouvelle_distance = distance+longueur_arc
                distance_min = dict_distance_min.get(successeur)
                if (distance_min is None or nouvelle_distance < distance_min):
                    # On met à jour egalement le predecesseur
                    dict_distance_min[successeur] = nouvelle_distance
                    dict_predecesseur[successeur] = noeud
                    file_priorite.insert(successeur, nouvelle_distance)
    distance = distance_min.get(arrivee)
    chemin = []
    if distance is not None:
        # Reconstruction du plus court chemin
        noeud = arrivee
        while noeud is not None:
            chemin = [noeud] + chemin
            noeud = dict_predecesseur.get(noeud)
            return (chemin, distance)
