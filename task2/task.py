from typing import Tuple
import math

def main(s: str, e: str) -> Tuple[float, float]:
    
    edges = [tuple(map(int, line.split(','))) for line in s.strip().split('\n')]
    nodes = sorted(set([u for u, v in edges] + [v for u, v in edges]))
    node_idx = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    adjacency = [[0]*n for _ in range(n)]
    for u, v in edges:
        adjacency[node_idx[u]][node_idx[v]] = 1

    relation = []
    for i in range(n):
        for j in range(n):
            if adjacency[i][j]:
                relation.append((i, j))

    total = len(relation)
    if total == 0:
        return 0.0, 0.0
    p = 1 / total

    H = - total * (p * math.log2(p))
    Hmax = math.log2(n*n)
    K = H / Hmax if Hmax != 0 else 0.0

    return round(H, 1), round(K, 1)

print("TEST", '\n')
csv_str = "1,2\n1,3\n3,4\n3,5\n5,6\n6,7"
root = "1"
print(main(csv_str, root))
