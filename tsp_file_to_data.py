import math

def euclidean_distance(coord1, coord2):
    return math.ceil(math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2))

# Given .tsp data
tsp_data = """
1 38.24 20.42
2 39.57 26.15
3 40.56 25.32
4 36.26 23.12
5 33.48 10.54
6 37.56 12.19
7 38.42 13.11
8 37.52 20.44
9 41.23 9.10
10 41.17 13.05
11 36.08 -5.21
12 38.47 15.13
13 38.15 15.35
14 37.51 15.17
15 35.49 14.32
16 39.36 19.56
17 38.09 24.36
18 36.09 23.00
19 40.44 13.57
20 40.33 14.15
21 40.37 14.23
22 37.57 22.56
"""

# Parse the .tsp data
lines = tsp_data.strip().split('\n')
coordinates = [list(map(float, line.split()[1:])) for line in lines]

# Calculate Euclidean distances
dimension = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(dimension)] for i in range(dimension)]

# Print the distance matrix
for row in distance_matrix:
    print(f"{row},")
