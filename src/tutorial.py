import networkx as nx

def create_graph(edges: list[tuple[int, int]]) -> nx.Graph:
    
    G = nx.Graph()
    
   
    G.add_edges_from(edges)
    
    
    return G

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 6)]
G = create_graph(edges)


print(G.nodes)  
print(G.edges)  

def get_degree(G: nx.Graph, node: int) -> int:
    
    return G.degree(node)

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 6)]
G = nx.Graph(edges)


degree = get_degree(G, 2)
print(f"Derajat simpul 2: {degree}")  

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    visited = set()  
    result = []  

    def dfs(node):
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in sorted(G.neighbors(node)):  
                dfs(neighbor)

    dfs(start)
    return result

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 6)]
G = nx.Graph(edges)


dfs_result = dfs_traversal(G, 1)
print(f"Urutan DFS: {dfs_result}")



from collections import deque

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
   
    visited = set()  
    queue = deque([start])  
    result = []  

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in sorted(G.neighbors(node)):  
                if neighbor not in visited:
                    queue.append(neighbor)

    return result
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 6)]
G = nx.Graph(edges)


bfs_result = bfs_traversal(G, 1)
print(f"Urutan BFS: {bfs_result}")



def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    
    try:
        return nx.shortest_path(G, source=source, target=target)
    except nx.NetworkXNoPath:
        return [] 

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 6)]
G = nx.Graph(edges)


shortest_path = find_shortest_path(G, 1, 6)
print(f"Jalur terpendek dari 1 ke 6: {shortest_path}")



import matplotlib.pyplot as plt

def visualize_graph(G: nx.Graph) -> None:
    
    plt.figure(figsize=(8, 6))  
    pos = nx.spring_layout(G)  
    
  
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10)
    
    
    plt.savefig("graph_visualization.png", format="png", dpi=300)
    
    
    plt.show()

edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (5, 6)]
G = nx.Graph(edges)


visualize_graph(G)