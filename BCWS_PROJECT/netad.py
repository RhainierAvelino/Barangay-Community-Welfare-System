import matplotlib.pyplot as plt
import networkx as nx

# Create a graph
G = nx.Graph()

# Add nodes
G.add_node("Internet")
G.add_node("Proxy Firewall")
G.add_node("Main Router")
G.add_node("Internal Switch (VLAN 10)")
G.add_node("Guest Switch (VLAN 20)")
G.add_node("Internal APs")
G.add_node("Guest APs")
G.add_node("IDS/IPS")
G.add_node("App Server")
G.add_node("DB Server")
G.add_node("File Server")
G.add_node("Workstation 1")
G.add_node("Workstation 2")
G.add_node("Workstation 3")
G.add_node("Guest Device 1")
G.add_node("Guest Device 2")

# Add edges
G.add_edges_from([
    ("Internet", "Proxy Firewall"),
    ("Proxy Firewall", "Main Router"),
    ("Proxy Firewall", "IDS/IPS"),
    ("Main Router", "Internal Switch (VLAN 10)"),
    ("Main Router", "Guest Switch (VLAN 20)"),
    ("Internal Switch (VLAN 10)", "Internal APs"),
    ("Internal Switch (VLAN 10)", "App Server"),
    ("Internal Switch (VLAN 10)", "DB Server"),
    ("Internal Switch (VLAN 10)", "File Server"),
    ("Internal Switch (VLAN 10)", "Workstation 1"),
    ("Internal Switch (VLAN 10)", "Workstation 2"),
    ("Internal Switch (VLAN 10)", "Workstation 3"),
    ("Guest Switch (VLAN 20)", "Guest APs"),
    ("Guest APs", "Guest Device 1"),
    ("Guest APs", "Guest Device 2")
])

# Define positions for nodes
pos = {
    "Internet": (0, 5),
    "Proxy Firewall": (1, 5),
    "Main Router": (2, 5),
    "IDS/IPS": (1, 4),
    "Internal Switch (VLAN 10)": (3, 6),
    "Guest Switch (VLAN 20)": (3, 4),
    "Internal APs": (4, 6),
    "Guest APs": (4, 4),
    "App Server": (5, 7),
    "DB Server": (5, 6),
    "File Server": (5, 5),
    "Workstation 1": (6, 7),
    "Workstation 2": (6, 6),
    "Workstation 3": (6, 5),
    "Guest Device 1": (5, 3),
    "Guest Device 2": (5, 2)
}

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
plt.title("PrizmTech Inc. Network Diagram")
plt.show()
