import sys, os
from Bio import SeqIO

def kmers(seq, k):
    return [seq[i:i + k] for i in range(len(seq) - k)]

class Node:
    """docstring for Node."""

    def __init__(self, label, adj_list, in_degree, out_degree):
        self.label = label
        self.adj_list = adj_list
        self.in_degree = 0
        self.out_degree = 0

    def add_adj(self, label):
        is_adj, index = self.is_adj(label)
        if is_adj:
            self.adj_list[index][1] += 1
        else:
            self.adj_list.append([label, 1])

    def is_adj(self, label):
        for i, edge in enumerate(self.adj_list):
            if edge[0] == label:
                return True, i
        return False, -1


class Graph:
    """docstring for Graph."""

    def __init__(self, node_list=[]):
        self.node_list = node_list

    def add_node(self, label):
        node = self.find_node(label)
        if node is None:
            new_node = Node(label, [], 0, 0)
            self.node_list.append(new_node)
            return new_node
        else:
            return node

    def find_node(self, label):
        for node in self.node_list:
            if node.label == label:
                return node
        return None

    def print_graph(self):
        with open('out.txt', 'w') as f:
            for node in self.node_list:
                output = "" + node.label + " : "
                for adj_node in node.adj_list:
                    output += "(" + adj_node[0] + ", " + str(adj_node[1]) +") "
                print(output, file=f)

def build(fn, k=31):

    G = Graph()

    records = SeqIO.parse(fn, 'fastq')

    # records = [record for i, record in enumerate(records) if i < 50]

    for record in records:

        seq = str(record.seq)

        for kmer in kmers(seq, k):

            src = G.add_node(kmer[0:k-1])
            dest = G.add_node(kmer[1:k])

            src.out_degree += 1
            src.add_adj(dest.label)

            dest.in_degree += 1

    return G

try:
    fn = sys.argv[1]
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(fn):
    raise SystemError("Error: File does not exist\n")

G = build(fn)

G.print_graph()
