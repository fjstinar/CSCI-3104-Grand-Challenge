import sys, os
from Bio import SeqIO

class Node(object):
    """docstring for Node."""

    def __init__(self, km):
        self.kmer = km
        self.in_degree = 0
        self.out_degree = 0

class Edge(object):
    """docstring for Edge."""

    def __init__(self, km):
        self.kmer = km

def build(fn, k=31):
    adj_list = dict()
    vertices = dict()

    records = SeqIO.parse(fn, 'fastq')

    for record in records:

        seq = str(record.seq)

        for i in range(len(seq) - k):
            v1 = seq[i:i+k]
            v2 = seq[i+1:i+k+1]

            if v1 in adj_list.keys():
                vertices[v1].out_degree += 1
                adj_list[v1].append(Edge(v2))
            else:
                vertices[v1] = Node(v1)
                vertices[v1].out_degree += 1
                adj_list[v1] = [Edge(v2)]

            if v2 in adj_list.keys():
                vertices[v2].in_degree += 1
            else:
                vertices[v2] = Node(v2)
                vertices[v2].in_degree += 1
                adj_list[v2] = []

    return (vertices, adj_list)

def print_graph(g):
    """ Print the information in the graph to be (somewhat) presentable """
    V = g[0]
    E = g[1]
    for k in V.keys():
        print("name: ", V[k].kmer, ". indegree: ", V[k].in_degree, ". outdegree: ", V[k].out_degree)
        print("Edges: ")
        for e in E[k]:
            print(e.kmer)
        print()

def output_contigs(g):
    """ Perform searching for Eulerian path in the graph to output genome assembly"""
    V = g[0]
    E = g[1]
    # Pick starting node (the vertex with zero in degree)
    start = list(V.keys())[0]
    for k in V.keys():
        if V[k].in_degree < V[start].in_degree:
            start = k

    contig = start
    current = start
    while len(E[current]) > 0:
        # Pick the next node to be traversed (for now, at random)
        next = E[current][0]
        del E[current][0]
        contig += next.kmer[-1]
        current = next.kmer

    return contig

try:
    fn = sys.argv[1]
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(fn):
    raise SystemError("Error: File does not exist\n")

print(output_contigs(build(fn)))
