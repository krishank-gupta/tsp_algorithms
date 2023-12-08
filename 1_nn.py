import sys
from data import distance_matrix
import time
import psutil

def nearest_neighbor(distance_matrix):
    num_cities = len(distance_matrix)
    unvisited_cities = set(range(num_cities))
    current_city = 0  # Start from the first city
    tour = [current_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distance_matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    return tour

def calculate_tour_length(tour, distance_matrix):
    length = 0
    for i in range(len(tour) - 1):
        length += distance_matrix[tour[i]][tour[i + 1]]
    length += distance_matrix[tour[-1]][tour[0]]
    return length

start = time.time()

cpu_before = psutil.cpu_percent(interval=None)
memory_before = psutil.virtual_memory().percent

tour = nearest_neighbor(distance_matrix)
tour_length = calculate_tour_length(tour, distance_matrix)

end = time.time()

cpu_after = psutil.cpu_percent(interval=None)
memory_after = psutil.virtual_memory().percent

print("Tour Length:", tour_length)
print("Time:", end-start)
print(f"CPU Usage: {cpu_after - cpu_before}%")
print(f"Memory Usage: {memory_after - memory_before}%")
