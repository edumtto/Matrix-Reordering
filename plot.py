import functools
import graphviz as gv

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

styles = {
    'graph': {
        'overlap':'scale',
        'splines':'true',
        'fontsize': '14',
        'fontcolor': 'white',
        'bgcolor': '#333333',
        'rankdir': 'BT'
    },
    'nodes': {
        'fontname': 'Helvetica',
        'shape': 'circle',
        'fontcolor': 'white',
        'color': 'white',
        'style': 'filled',
        'fillcolor':'#006699'
    },
    'edges': {
        'style': 'solid',
        'color': 'white',
        'arrowhead': 'open',
        'fontname': 'Courier',
        'fontsize': '12',
        'fontcolor': 'white',
    }
}

def show_graph_pyplot(adj_mat):
    g = nx.from_numpy_matrix(np.array(adj_mat)) 
    nx.draw(g, with_labels=True)
    plt.show()

def add_nodes(graph, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            graph.node(n[0], **n[1])
        else:
            graph.node(n)
    return graph

def add_edges(graph, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            graph.edge(*e[0], **e[1])
        else:
            graph.edge(*e)
    return graph

def apply_styles(graph, styles):
    graph.graph_attr.update(
        ('graph' in styles and styles['graph']) or {}
    )
    graph.node_attr.update(
        ('nodes' in styles and styles['nodes']) or {}
    )
    graph.edge_attr.update(
        ('edges' in styles and styles['edges']) or {}
    )
    return graph

def plot_graph(adj_mat, name, visited = None):
    dimension = len(adj_mat)
    
    nodes = []
    if visited is None:
        nodes = [str(i) for i in range(dimension)]
    else:
        nodes = [(str(i), {'style': 'filled', 
                            'fillcolor': 'red' if visited[i] else '#006699'
                            }) for i in range(dimension)]
    
    edges = []
    for i in range(dimension-1):
        for j in range(i+1, dimension):
            if adj_mat[i][j] != 0:
              edges.append( (str(i), str(j)) )

    graph = functools.partial(gv.Graph, format='svg')
    g = graph()
    
    g = apply_styles(g, styles)
    
    g = add_nodes(g, nodes)
    g = add_edges(g, edges)
    
    g.render('img/g')