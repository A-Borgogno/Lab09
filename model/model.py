import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._aeroporti = DAO.getAllAeroporti()
        self._grafo = nx.Graph()
        self.buildGraph()
        self._idMapAeroporti = {}
        for a in self._aeroporti:
             self._idMapAeroporti[a.ID] = a

    def buildGraph(self):
        # Aggiungiamo i nodi
        self._grafo.add_nodes_from(self._aeroporti)

    def analizza(self, distanza):
        self._grafo.clear_edges()
        self.addEdges(distanza)
        return self._grafo

    def addEdges(self, distanza):
        edges = DAO.getAllEdges(distanza)
        for edge in edges:
            self._grafo.add_edge(self._idMapAeroporti[edge[0]], self._idMapAeroporti[edge[1]], weight=edge[2])
