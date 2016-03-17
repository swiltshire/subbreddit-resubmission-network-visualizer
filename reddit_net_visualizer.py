import networkx as nx
import csv
import numpy as np
import pydot
import functools
import graphviz as gv
import matplotlib.pyplot as plt

graph = pydot.Dot(graph_type='digraph', rankdir='LR', size = "20, 10", layout = "dot", outputorder = "nodesfirst", maxiter = "10000", nodesep = ".25", ranksep = ".5", overlap = "scale", splines = "spline", spline = "true")
graph.set_node_defaults(fontname = "Adobe Garamond Pro", fontsize="60", penwidth="1")
graph.set_edge_defaults(fontname = "Adobe Garamond Pro", arrowhead = "normal", arrowtail = "inv", dir="both")

# read_file = open('subreddit_resubmission_links.txt', 'r')
# networkx_graph = nx.read_edgelist(read_file, delimiter='\t', create_using=nx.DiGraph(), nodetype=str, data=(('weight',float),))
# read_file.close()
#
# nodes_by_out_degree = nx.out_degree_centrality(networkx_graph)
#
# for node in reversed(sorted(nodes_by_out_degree, key=nodes_by_out_degree.get)):
# 	graph.add_node(pydot.Node(str(node)))

read_file = open('subreddit_resubmission_links.txt', 'r')

file_reader = csv.reader(read_file, delimiter = '\t')
for edge in file_reader:
	if int(edge[2]) > 10 and edge[0] != edge[1]:
		src = pydot.Node(str(edge[0]))
		dest = pydot.Node(str(edge[1]))
		weight = int(edge[2])
		# penwidth = .25+np.log(.25*weight)
		penwidth = .25 + np.log10(.09*weight)
		color = '#000000'
		if weight < 50:
			color = "#550000"
		elif 50 <= weight < 100:
			color = "#660000"
		elif 100 <= weight < 200:
			color = "#770000"
		elif 200 <= weight < 400:
			color = "#880000"
		elif 400 <= weight < 800:
			color = "#990000"
		elif 800 <= weight < 1600:
			color = "#AA0000"
		elif 1600 <= weight < 3200:
			color = "#BB0000"
		elif 3200 <= weight < 6400:
			color = "#CC0000"
		elif 6400 <= weight:
			color = "#DD0000"
		# graph.add_edge(pydot.Edge(src, dest, label=" "+ str(weight), color = color, penwidth=str(penwidth)))
		graph.add_edge(pydot.Edge(src, dest, color = color, penwidth=str(penwidth)))
read_file.close()

# graph.savefig('myimage.svg', format='svg', dpi=1200)

graph.write('graph1.svg', format='svg')