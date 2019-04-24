def getOverlap(left, right):
    if left == right[-len(left):]:
        return left
    i = -1
    while True:
        temp = left[0:i]
        if temp == right[-len(temp):]:
            return len(temp)
        elif temp == "":
            return 0
        i -= 1

class Graph(object):

    def __init__(self, V=None):
        self.__adj_list = __generate_graph(V)

    def __generate_graph(self, V):
        self.__adj_list = {}
        for src in V:
            self.__adj_list[src['name']] = []
            for dest in V:
                if src != dest:
                    w = getOverlap(src['sequence'], dest['sequence'])
                    self.__adj_list[src['name']].append((dest['name'], w))

    def __generate_edges(self):
        edges = []
        for vertex in self.__adj_list:
            for neighbour in self.__adj_list[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__adj_list:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
