import json
import os
import re
import csv
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt

# This script creates a network of people who helped each other in a Discord channel.
# It uses the help_network.json file created by the analyze_discord_chat.py script.
# The output are two network images, a file with network metrics, and the network file as a json.

# help_network.png shows the complete network. The nodes are colored by their community. 
# Community is detected using the Louvain algorithm.
# labels are omitted for clarity

# core_network.png shows the core of the community based on the help network. these are a tightly
# knit group of members who help each other. 

# Disclaimer:
# the data parsing isn't perfect. This is a poc to show what could be done with the data.

# Future work (beyond better data parsing):
# assign expertise areas based on help given and received
# rewards those with hub powers as they are the "glue" between members

# Create output directory if it doesn't exist
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)

def parse_names(name_string):
    # Remove square brackets and @ symbols, then split by |
    clean_string = name_string.strip('[]').replace('@', '')
    return [name.strip() for name in clean_string.split('|')]

def process_help_entry(entry):
    # Updated pattern to handle various formats including @ symbols
    pattern = r'[@\[]?(.*?)[\]]?\s+helped\s+[@\[]?(.*?)[\]]?\s+with\s+(.*?)(?:\s+by\s+providing\s+.*)?$'
    match = re.match(pattern, entry, re.IGNORECASE)
    
    if not match:
        print(f"Warning: Could not parse entry: {entry}")
        return []
    
    helpers = parse_names(match.group(1))
    helped = parse_names(match.group(2))
    help_type = match.group(3).strip()
    
    # Create edges as (u, v, {attr_dict}) format for NetworkX
    edges = []
    for helper in helpers:
        for helped_person in helped:
            edges.append((helper, helped_person, {'help_type': help_type}))
    
    return edges

def create_edge_list(directory_path):
    edges = []
    directory = Path(directory_path)
    
    for json_file in directory.glob('*.json'):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for date_key in data:
                help_entries = data[date_key].get("Who Helped Who", [])
                for entry in help_entries:
                    edges.extend(process_help_entry(entry))
    
    return edges

def create_network(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def show_network(G):
    plt.figure(figsize=(12, 8))
    colors = [G.nodes[node]['community'] for node in G.nodes()]
    nx.draw(G, with_labels=False, node_color=colors)
    plt.savefig(output_dir / 'help_network.png', bbox_inches='tight')
    plt.close()

def show_core_network(G):
    # turn graph into undirected
    U = G.to_undirected()
    
    # Show the largest connected component
    largest_cc = max(nx.connected_components(U), key=len)
    G_largest = G.subgraph(largest_cc)
    
    plt.figure(figsize=(12, 8))
    colors = [G_largest.nodes[node]['community'] for node in G_largest.nodes()]
    nx.draw(G_largest, with_labels=False, node_color=colors)
    plt.savefig(output_dir / 'core_network.png', bbox_inches='tight')
    plt.close()

def detect_communities(G):
    # Get community 
    communities = nx.community.louvain_communities(G)
    
    # Assign each node its community number
    community_map = {}
    for i, community in enumerate(communities):
        for node in community:
            community_map[node] = i
            
    # Update node attributes with community number
    nx.set_node_attributes(G, community_map, 'community')
    
    return communities, community_map

def calculate_metrics(G, communities):
    size = nx.number_of_nodes(G)
    density = nx.density(G)
    print(f"Size: {size}")
    print(f"Density: {density}")
    print(f"Number of communities: {len(communities)}")

    # Calculate degree (influence)
    deg = dict(nx.degree(G))
    print("\nTop 5 most helpful people:")
    for node, degree in sorted(deg.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{node}: {degree}")

    # Calculate betweenness centrality (hub-power)
    btw = nx.betweenness_centrality(G)
    print("\nTop 5 nodes by betweenness centrality:")
    for node, cent in sorted(btw.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{node}:{cent:.3f}")

    # Calculate closeness centrality (hub-power)
    clo = nx.closeness_centrality(G)
    print("\nTop 5 nodes with hub-power centrality:")
    for node, cent in sorted(clo.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"{node}:{cent:.3f}")

    return deg, btw, clo

def metrics_to_csv(G, communities, deg, btw, clo):
    with open(output_dir / 'metrics.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Node', 'Community', 'Degree', 'Betweenness Centrality', 'Closeness Centrality'])
        for node in G.nodes():
            writer.writerow([node, communities[node], deg[node], btw[node], clo[node]])

def main():
    directory_path = 'samples/coders_out'
    edges = create_edge_list(directory_path)
    G = create_network(edges)
    comms, comm_map = detect_communities(G)
    
    # Capture the returned metrics
    deg, btw, clo = calculate_metrics(G, comms)
    
    # create visualizations
    show_network(G)
    show_core_network(G)
    
    # save metrics
    metrics_to_csv(G, comm_map, deg, btw, clo)
    
    # Save as JSON for NetworkX
    network_data = {
        'edges': list(G.edges(data=True))
    }
    
    with open(output_dir / 'help_network.json', 'w', encoding='utf-8') as f:
        json.dump(network_data, f, indent=2)

if __name__ == "__main__":
    main() 