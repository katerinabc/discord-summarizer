# Discord Chat Network

A Python script that analyzes comprehensive summaries of Discord chat exports. The analyzes focuses on the section "Who Helped Who" and extracts from the first sentence the involved people and the topic of help. 

Repo to create the discord chat summaries: https://github.com/elizaOS/discord-summarizer

## Features

- **Influence metrics**: Processes structured analysis of who is helping who and calculates:
  - How often someone helped another person (freeman degree centrality)
  - How easy it is to reach someone (betweeness centrality). These are your super-quick bridge-builders
  - How much hub power a person has (closeness centrality). These are harder to reach, but more aware of everything.

- **Community analysis**:
  - using the who is helping who network calculates the number of sub-communities using the Louvain algorithm
  - The output is used to calculate the number of silos, and color the nodes (ie members) in the networks

- **Core community**:
  - The core community is extracted (sub set of members who are helping each other a lot)
  - A graph is generated about this core
  - Nodes are colored based on their community group
  - Labels omitted

## Prerequisites

- Python 3.8+
- Required Python packages:
  ```
  newtorkx
  matplotlib
  ```

## Installation

1. Clone the repository or download the script
2. Install required packages:

```bash
pip install networkx matplotlib
```
3. Run the script making sure the input files are in the correct folder. 

## Usage

Basic usage:
```bash
python create_help_network.py 
```

## Output Format

The script generates the following files

1. **core_network.png**: Image of the core network
2. **help_network.json**: JSON of the network
3. **help_network.png**: Image of the complete network
4. **metrics.csv**: influence metrics for each node and their community number.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## To-do

- cateogrize help requests
- better parsing of who is helping who
