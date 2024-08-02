import sys

# 再帰の深さの上限を設定
LIMIT = 10000
sys.setrecursionlimit(LIMIT)


def depth_first_search(
    graph, node, visited, visited_edges, route_length, current_route
):
    """
    深さ優先探索を行い、そのノードでの最長経路を見つける。

    Args:
        graph (dict): グラフの隣接リスト表現
        node (int): 現在のノード
        visited (dict): 訪問したノードの記録
        visited_edges (set): 訪問したエッジの記録
        route_length (float): 現在の経路の長さ
        current_route (list): 現在の経路

    Returns:
        max_length (float): 見つかったそのノードでの最長経路の長さ
        longest_path (list): 見つかったそのノードでの最長経路
    """
    visited[node] = True
    current_route.append(node)
    max_length = route_length
    longest_path = current_route.copy()

    for neighbor, distance in graph[node]:
        if not visited[neighbor]:
            visited_edges.add((min(node, neighbor), max(node, neighbor)))
            current_length, current_path = depth_first_search(
                graph,
                neighbor,
                visited,
                visited_edges,
                route_length + distance,
                current_route
            )
            visited_edges.remove((min(node, neighbor), max(node, neighbor)))
            if max_length < current_length:
                max_length = current_length
                longest_path = current_path.copy()
        elif (min(node, neighbor), max(node, neighbor)) not in visited_edges:
            if max_length < route_length + distance:
                max_length = route_length + distance
                current_route.append(neighbor)
                longest_path = current_route.copy()
                current_route.pop()

    current_route.pop()
    visited[node] = False
    return max_length, longest_path


def find_longest_path(graph):
    """
    グラフ内の最長経路を見つける。

    Args:
        graph (dict): グラフの隣接リスト表現

    Returns:
        max_path_length (float): グラフ内の最長経路の長さ
        longest_path (list): グラフ内の最長経路
    """
    max_path_length = 0
    longest_path = []

    for node in graph:
        visited = {n: False for n in graph}
        visited_edges = set()
        initial_route_length = 0
        current_route = []

        temp_length, temp_path = depth_first_search(
            graph=graph,
            node=node,
            visited=visited,
            visited_edges=visited_edges,
            route_length=initial_route_length,
            current_route=current_route
        )

        if max_path_length < temp_length:
            max_path_length = temp_length
            longest_path = temp_path.copy()

    return max_path_length, longest_path


if __name__ == "__main__":
    # 入力データを受け取る
    input_data = sys.stdin.read().strip().split("\n")
    edges = [tuple(map(float, line.split(","))) for line in input_data]
    # グラフの隣接リスト表現を作成
    graph = {}
    for u, v, d in edges:
        u, v = int(u), int(v)
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, d))
        graph[v].append((u, d))

    max_length, route = find_longest_path(graph)
    # 結果を出力
    for node in route:
        print(f"{node}\r\n", end="")
