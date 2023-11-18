import networkx as nx
import numpy as np
from data import distance_matrix
import time
import psutil

def christofides(distance_matrix):
    num_cities = len(distance_matrix)

    # Step 1: Create a complete graph
    complete_graph = nx.Graph()
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            complete_graph.add_edge(i, j, weight=distance_matrix[i][j])

    # Step 2: Create a minimum spanning tree
    min_spanning_tree = nx.minimum_spanning_tree(complete_graph)

    # Step 3: Find odd-degree vertices in the minimum spanning tree
    odd_degree_vertices = [vertex for vertex, degree in min_spanning_tree.degree if degree % 2 != 0]

    # Step 4: Create a subgraph induced by odd-degree vertices
    subgraph_odd_degree = complete_graph.subgraph(odd_degree_vertices)

    # Step 5: Find a minimum-weight perfect matching in the subgraph
    min_weight_matching = nx.max_weight_matching(subgraph_odd_degree)

    # Step 6: Combine the minimum spanning tree and the matching to form a multigraph
    multigraph = nx.MultiGraph(min_spanning_tree)
    multigraph.add_edges_from(min_weight_matching)

    # Step 7: Find an Eulerian circuit in the multigraph
    eulerian_circuit = list(nx.eulerian_circuit(multigraph))

    # Step 8: Convert the Eulerian circuit into a Hamiltonian cycle
    visited = set()
    hamiltonian_cycle = [eulerian_circuit[0][0]]

    for edge in eulerian_circuit:
        if edge[1] not in visited:
            hamiltonian_cycle.append(edge[1])
            visited.add(edge[1])

    # Calculate the total length of the Hamiltonian cycle
    total_length = sum(distance_matrix[hamiltonian_cycle[i-1]][hamiltonian_cycle[i]] for i in range(num_cities))

    return total_length

def main():
    # Replace this matrix with your own data
    start = time.time()
    cpu_before = psutil.cpu_percent(interval=None)
    memory_before = psutil.virtual_memory().percent
    
    optimal_tour_length = christofides(distance_matrix)
    
    end = time.time()
    cpu_after = psutil.cpu_percent(interval=None)
    memory_after = psutil.virtual_memory().percent
    
    print("Optimal Tour Length (Christofides):", optimal_tour_length)
    print("Time:", end-start)
    print(f"CPU Usage: {cpu_after - cpu_before}%")
    print(f"Memory Usage: {memory_after - memory_before}%")
    
if __name__ == "__main__":
    main()
