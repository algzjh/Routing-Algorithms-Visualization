import random
import networkx as nx
import numpy as np
import json
import os
from datetime import datetime
import time


def write_to_json_file(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)


def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def createRandomGraph():
    construct_graph = {"nodes": [], "links": []}
    n = random.randint(5, 30)
    m = random.randint(n, min(2*n, n*(n-1)/2))
    G = nx.dense_gnm_random_graph(n, m, seed=np.random)
    print("n: ", n)
    print("m: ", m)
    print("G_n: ", G.number_of_nodes())
    print("G_m: ", G.number_of_edges())
    node_list = list(G.nodes)
    print(node_list)
    edge_list = list(G.edges)
    print(edge_list)
    for id in node_list:
        one_node = {"id": id+1, "name": str(id+1)}
        construct_graph["nodes"].append(one_node)
    for e in edge_list:
        w = random.randint(1, 100)
        one_edge = {"source": e[0]+1, "target": e[1]+1, "weight": w}
        construct_graph["links"].append(one_edge)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "static/RouteVisApp1/data/graph-random.json")
    write_to_json_file(filename, construct_graph)


if __name__ == "__main__":
    pass