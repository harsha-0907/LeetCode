# To draw the graphs
"""
import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
G.add_nodes_from([i for i in range(8)])

# Add edges
G.add_edges_from([(4, 7), (4, 5), (7, 6), (5, 6), (5, 2), (6, 2), (4, 3), (2, 3), (5, 1), (7, 0)])

# Draw the graph
nx.draw(G, with_labels=True, node_color='gold', node_size=1000, font_size=16, font_color='black')

# Display the graph
plt.show()"""

from google.cloud import idx

# Replace with your project ID and service account credentials
project_id = "your-project-id"
credentials = service_account.Credentials.from_service_account_file("path/to/your/service_account.json")

# Create a GraphServiceClient
client = idx.GraphServiceClient(project=project_id, credentials=credentials)

# Get a graph by ID
graph = client.get_graph(graph_id="your-graph-id")

# Print the graph's properties
print(graph)