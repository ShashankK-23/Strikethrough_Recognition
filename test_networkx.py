import networkx as nx
print(nx.__version__)  # Should display 3.4.2

# Test the gpickle functions
G = nx.Graph()
G.add_node(1)
G.add_edge(1, 2)

# Save and load using gpickle
nx.write_gpickle(G, "test_graph.pkl")
G_loaded = nx.read_gpickle("test_graph.pkl")

print("Graph loaded successfully:", G_loaded)
