from collections import deque
from typing import Dict, List, Optional, Set, Tuple


class Graph:
    def __init__(self):
        self.lista_adjacencia: Dict[str, List[str]] = {}

    def add_vertex(self, vertice: str) -> None:
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def add_edge(self, origem: str, destino: str, direcionado: bool = False) -> None:
        self.add_vertex(origem)
        self.add_vertex(destino)

        if destino not in self.lista_adjacencia[origem]:
            self.lista_adjacencia[origem].append(destino)

        if not direcionado:
            if origem not in self.lista_adjacencia[destino]:
                self.lista_adjacencia[destino].append(origem)

    def bfs(self, inicio: str) -> List[str]:
        if inicio not in self.lista_adjacencia:
            raise ValueError(f"O vértice '{inicio}' não existe no grafo.")

        visitados: Set[str] = {inicio}
        fila: deque[str] = deque([inicio])
        ordem: List[str] = []

        while fila:
            vertice = fila.popleft()
            ordem.append(vertice)

            for vizinho in sorted(self.lista_adjacencia[vertice]):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

        return ordem

    def shortest_path(self, inicio: str, destino: str) -> Optional[List[str]]:
        if inicio not in self.lista_adjacencia or destino not in self.lista_adjacencia:
            return None

        if inicio == destino:
            return [inicio]

        visitados: Set[str] = {inicio}
        fila: deque[Tuple[str, List[str]]] = deque([(inicio, [inicio])])

        while fila:
            vertice, caminho = fila.popleft()

            for vizinho in sorted(self.lista_adjacencia[vertice]):
                if vizinho == destino:
                    return caminho + [vizinho]

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vizinho]))

        return None


def demo() -> None:
    grafo = Graph()
    vertices = ["A", "B", "C", "D", "E", "F"]

    for vertice in vertices:
        grafo.add_vertex(vertice)

    arestas = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "F"),
        ("E", "F"),
    ]

    for origem, destino in arestas:
        grafo.add_edge(origem, destino)

    print("Busca em Largura:", grafo.bfs("A"))
    print("Menor caminho de A até F:", grafo.shortest_path("A", "F"))


if __name__ == "__main__":
    demo()
