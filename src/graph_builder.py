import networkx as nx
import os
import pickle

# Graph model path
graph_path = os.path.join("models", "graph.pkl")

# Ensure the models folder exists
os.makedirs("models", exist_ok=True)

# Create a sample graph
G = nx.Graph()
G.add_node(1, label="Start")
G.add_node(2, label="End")
G.add_edge(1, 2, weight=5)

# Save the graph using pickle
try:
    with open(graph_path, "wb") as f:
        pickle.dump(G, f)
    print(f"✅ Graph saved successfully at: {graph_path}")

    # Load the graph for verification
    with open(graph_path, "rb") as f:
        G_loaded = pickle.load(f)

    print("✅ Graph loaded successfully:")
    print(G_loaded.nodes(data=True))
    print(G_loaded.edges(data=True))

except Exception as e:
    print(f"❌ Error saving/loading graph: {e}")
