import sys
from itertools import combinations
from data import distance_matrix
import time
import psutil

def held_karp(distance_matrix):
    num_cities = len(distance_matrix)
    memo = {}

    # Function to calculate the cost of the optimal tour starting from the source city
    def tsp(mask, current_city):
        if (mask, current_city) in memo:
            return memo[(mask, current_city)]

        if mask == (1 << num_cities) - 1:  # All cities visited
            return distance_matrix[current_city][0]  # Return to the starting city

        min_cost = sys.maxsize

        for next_city in range(num_cities):
            if mask & (1 << next_city) == 0:  # Check if next_city is not visited
                new_mask = mask | (1 << next_city)
                cost = distance_matrix[current_city][next_city] + tsp(new_mask, next_city)
                min_cost = min(min_cost, cost)

        memo[(mask, current_city)] = min_cost
        return min_cost

    start_mask = 1
    return tsp(start_mask, 0)

def main():
    cpu_before = psutil.cpu_percent(interval=None)
    memory_before = psutil.virtual_memory().percent
    start = time.time()
    optimal_tour_length = held_karp(distance_matrix)
    end = time.time()
    cpu_after = psutil.cpu_percent(interval=None)
    memory_after = psutil.virtual_memory().percent
    print("Optimal Tour Length (Held-Karp):", optimal_tour_length)
    print("Time:", end-start)
    print(f"CPU Usage: {cpu_after - cpu_before}%")
    print(f"Memory Usage: {memory_after - memory_before}%")
if __name__ == "__main__":
    main()
