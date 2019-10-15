# Library for INT_MAX
import sys
import json
from copy import deepcopy


def read_json_file(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def change2INF(dist):
    d1 = deepcopy(dist)
    for i in range(len(d1)):
        if d1[i] == sys.maxsize:
            d1[i] = "INF"
    print(d1)
    return d1

def getDijkstra(graph_data, start_node, end_node):
    result = {}
    add_list = []
    nodes = graph_data["nodes"]
    links = graph_data["links"]
    nodes_tot = len(nodes)
    cost_matrix = [[sys.maxsize for i in range(nodes_tot + 1)] for j in range(nodes_tot + 1)]
    dist = [sys.maxsize for i in range(nodes_tot + 1)]
    vis = [False for i in range(nodes_tot + 1)]
    for item in links:
        u = item["source"]
        v = item["target"]
        w = item["weight"]
        if cost_matrix[u][v] > w:
            cost_matrix[u][v] = cost_matrix[v][u] = w
    dist[int(start_node)] = 0
    round = 0
    result[round] = deepcopy(dist)
    while True:
        round += 1
        k = -1
        mi = sys.maxsize
        for i in range(1, nodes_tot+1):
            if vis[i] is False and dist[i] < mi:
                mi = dist[i]
                k = i
        if k == -1:
            break
        add_list.append(k)
        vis[k] = True
        for i in range(1, nodes_tot + 1):
            if vis[i] is False and dist[k] + cost_matrix[k][i] < dist[i]:
                dist[i] = dist[k] + cost_matrix[k][i]
        result[round] = change2INF(dist)
    return result, add_list


if __name__ == "__main__":
    filename = "./static/RouteVisApp1/data/example-graph.json"
    graph_data = read_json_file(filename)
    print(graph_data)
    start_node = "5"
    end_node = "1"
    result, add_list = getDijkstra(graph_data, start_node, end_node)
    print("result: \n", result)
    print("add_list: \n", add_list)
    """
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
    g.dijkstra(0)
    """
