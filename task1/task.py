from typing import List, Tuple

def main(s: str, e: str) -> Tuple[
    List[List[bool]],
    List[List[bool]],
    List[List[bool]],
    List[List[bool]],
    List[List[bool]]
]:
    edges = [tuple(map(int, line.split(','))) for line in s.strip().split('\n')]
    nodes = set()
    for u, v in edges:
        nodes.add(u)
        nodes.add(v)
    nodes = sorted(nodes)
    node_idx = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[node_idx[u]].append(node_idx[v])

    direct = [[False]*n for _ in range(n)]
    for u, v in edges:
        direct[node_idx[u]][node_idx[v]] = True

    access = [[False]*n for _ in range(n)]
    def dfs_access(u, orig):
        for v in adj[u]:
            access[orig][v] = True
            dfs_access(v, orig)
    for i in range(n):
        dfs_access(i, i)

    reverse_access = [[False]*n for _ in range(n)]
    parents = [[] for _ in range(n)]
    for u, v in edges:
        parents[node_idx[v]].append(node_idx[u])
    def dfs_reverse(u, orig):
        for p in parents[u]:
            reverse_access[orig][p] = True
            dfs_reverse(p, orig)
    for i in range(n):
        dfs_reverse(i, i)

    parent_relation = [[False]*n for _ in range(n)]
    for u, v in edges:
        parent_relation[node_idx[v]][node_idx[u]] = True

    identity = [[i == j for j in range(n)] for i in range(n)]

    return direct, access, reverse_access, parent_relation, identity



print("TEST", '\n')
print('---------------')

csv_str = "1,2\n1,3\n3,4\n3,5\n5,6\n6,7"
root = "1"
matrices = main(csv_str, root)
for idx, m in enumerate(matrices):
    print(f"Matrix {idx+1}:")
    for row in m:
        print(row)
    print('---------------', '\n')
