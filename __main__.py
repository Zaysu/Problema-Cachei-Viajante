import math
import itertools

def tsp_bruteforce(distances, n):
    min_distance = float('inf')
    for perm in itertools.permutations(range(n)):
        distance = 0
        for i in range(n - 1):
            distance += distances[perm[i]][perm[i + 1]]
        distance += distances[perm[-1]][perm[0]] 
        min_distance = min(min_distance, distance)
    return min_distance

def tsp_dp(distances, n):
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  

    for mask in range(1, 1 << n):
        for u in range(n):
            if mask & (1 << u):  
                for v in range(n):
                    if not (mask & (1 << v)):  
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + distances[u][v])


    return min(dp[(1 << n) - 1][i] + distances[i][0] for i in range(1, n))

def tsp_nearest_neighbor(distances, n):

    visited = [False] * n
    visited[0] = True
    tour = [0]
    current_city = 0
    total_distance = 0

    for _ in range(n - 1):
        next_city = -1
        nearest_distance = float('inf')
        for city in range(n):
            if not visited[city] and distances[current_city][city] < nearest_distance:
                next_city = city
                nearest_distance = distances[current_city][city]
        visited[next_city] = True
        tour.append(next_city)
        total_distance += nearest_distance
        current_city = next_city

    total_distance += distances[current_city][0]
    return total_distance

def tsp_n2(distances, n):
    min_distance = float('inf')
    for i in range(n):
        distance = 0
        for j in range(n):
            if i != j:
                distance += distances[i][j]
        min_distance = min(min_distance, distance)
    return min_distance

def tsp_log_n(distances, n):
    return math.log(n)

def read_data(file_name):
    with open(file_name, 'r') as file:
        n = int(file.readline().strip())
        distances = [list(map(int, file.readline().strip().split())) for _ in range(n)]
    return distances, n

def test_tsp(file_name):
    print(f"\nTestando com o arquivo: {file_name}")
    try:
        distances, n = read_data(file_name)

        print("Resultado O(log n):", tsp_log_n(distances, n))
        print("Resultado O(n²):", tsp_n2(distances, n))
        print("Resultado O(n!): Força bruta", tsp_bruteforce(distances, n))
        print("Resultado O(n²): Programação dinâmica", tsp_dp(distances, n))
        print("Resultado O(n²): Vizinhança mais próxima", tsp_nearest_neighbor(distances, n))
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    files = [
        'tsp_small.txt',
        'tsp_medium.txt',
        'tsp_large.txt'
    ]

    for file_name in files:
        test_tsp(file_name)