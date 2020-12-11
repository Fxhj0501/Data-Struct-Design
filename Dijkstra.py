# Dijkstra.狄杰斯特拉
import heapq
import math
from ReadFile import road
from ReadFile import manage_station

def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra(s):
    graph = manage_station
    path = []
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)

    while len(pqueue) > 0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(s)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if dist + float(graph[vertex][w]) < distance[w]:
                    heapq.heappush(pqueue, (dist + float(graph[vertex][w]), w))
                    parent[w] = vertex
                    distance[w] = dist + float(graph[vertex][w])
    return parent, distance

def serach_path(start,parent_dict,destination,path):
    while parent_dict[destination]!=start:
        path.append(parent_dict[destination])
        destination = parent_dict[destination]
    path.append(start)
    return path

def cal_ticket(distance):
    if distance>=0 and distance<6:
        return 3
    elif distance>=6 and distance<12:
        return 4
    elif distance>=12 and distance<22:
        return 5
    elif distance>=22 and distance<32:
        return 6
    else :
        k = 1
        while True:
            if distance - 32 < k * 20:
                return 6 + k
            else:
                k = k + 1
                continue



