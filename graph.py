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
