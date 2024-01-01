def add_node(v):
    global node_count
    if v in nodes:
        print('node is already present')
    else:
        node_count = node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

# def add_edge(v1, v2): # undirected unweighted graph
#     if v1 not in nodes:
#         print(v1,'is not present')
#     elif v2 not in nodes:
#         print(v2,'is not present')
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 1
#         graph[index2][index1] = 1
        
# def add_edge(v1, v2, cost): # undirected weighted graph
#     if v1 not in nodes:
#         print(v1,'is not present')
#     elif v2 not in nodes:
#         print(v2,'is not present')
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = cost
#         graph[index2][index1] = cost
        
def add_edge(v1, v2, cost): # directed weighted graph
    if v1 not in nodes:
        print(v1,'is not present')
    elif v2 not in nodes:
        print(v2,'is not present')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost

# def add_edge(v1, v2): # directed unweighted graph
#     if v1 not in nodes:
#         print(v1,'is not present')
#     elif v2 not in nodes:
#         print(v2,'is not present')
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 1

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,'is not present')
    else:
        index1 = nodes.index(v) 
        node_count = node_count -1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

# def delete_edge(v1,v2): # undirected and weighted or unweighted graph
#     if v1 not in nodes:
#         print(v1,'is not present')
#     elif v2 not in nodes:
#         print(v2,'is not present')
#     else:
#         index1 = nodes.index(v1)
#         index2 = nodes.index(v2)
#         graph[index1][index2] = 0
#         graph[index2][index1] = 0
            
def delete_edge(v1,v2): # directed and weighted or unweighted graph
    if v1 not in nodes:
        print(v1,'is not present')
    elif v2 not in nodes:
        print(v2,'is not present')
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 0

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], '<3'), end=' ')
        print()


nodes = []
graph = []
node_count = 0
add_node('A')
add_node('B')
add_node('C')
add_edge('A','B',10)
add_edge('A','C',5)
delete_edge('A','C')
print('nodes:',nodes)
print_graph()