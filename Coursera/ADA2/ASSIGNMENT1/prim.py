'''
Question 3
In this programming problem you'll code up Prim's minimum spanning tree algorithm. Download the text file here. This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
'''

from dijkstra import PriorityQueue as PQ
from collections import defaultdict


def Prim(source, pq, edges):
    """Prim's algorithm to calculate minimum_spanning_tree (MST), the idea
is very similar to Dijkstra's shortest path. Operations based on priority
queue make the running time of O(mlogn), where m is the number of edges
and n is the number of nodes. Tricky part is to update the connected nodes'
cheapest edge distance when a node is added to 'processed'."""
    
    processed = [source]
    mst = []
    uncharted = set([i[1] for i in pq.heap])
    while len(uncharted) != 0:
        cheapest_edge_dist, new_node = pq.pop()
        processed.append(new_node)
        mst.append(cheapest_edge_dist)
        uncharted.remove(new_node)
        for head, edge_dist in edges[new_node]:
            if head in uncharted:
                old_dist = pq.delete(head)
                new_dist = min(old_dist, edge_dist)
                pq.insert(head, new_dist)
    return mst


def main():
    edges = defaultdict(list)
    heap = []
    source = 1
    BIG = 1000000000
    with open('edges.txt') as file_in:
    #with open('primcase.txt') as file_in:
        for i, line in enumerate(file_in):
            x = line.strip().split()
            if i == 0:
                number_of_nodes = int(x[0])
            else:
                head, tail, edge_dist = int(x[0]), int(x[1]), int(x[2])
                edges[head].append((tail, edge_dist))
                edges[tail].append((head, edge_dist))
    source_edges = dict(edges[source])
    for node in range(2, number_of_nodes + 1):
        if node in source_edges.keys():
            heap.append([source_edges[node], node])
        else:
            heap.append([BIG, node])
    pq = PQ(heap)
    mst_edges = Prim(1, pq, edges)
    return sum(mst_edges)


if __name__ == '__main__':
    print main()