def add_node(v):
    if v in graph:
        print(v,'is already present')
    else:
        graph[v] = []

def add_edge(v1,v2): # undirected unweighted graph
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else:
       graph[v1].append(v2) 
       graph[v2].append(v1) 

# def add_edge(v1,v2, cost): # undirected weighted graph
#     if v1 not in graph:
#         print(v1,'is not present')
#     elif v2 not in graph:
#         print(v2,'is not present')
#     else:
#        list1 = [v2,cost]
#        list2 = [v1,cost]
#        graph[v1].append(list1) 
#        graph[v2].append(list2) 
        
# def add_edge(v1,v2, cost): # directed weighted graph
#     if v1 not in graph:
#         print(v1,'is not present')
#     elif v2 not in graph:
#         print(v2,'is not present')
#     else:
#        list1 = [v2,cost]
#        graph[v1].append(list1) 
        
# def add_edge(v1,v2): # directed unweighted graph
#     if v1 not in graph:
#         print(v1,'is not present')
#     elif v2 not in graph:
#         print(v2,'is not present')
#     else:
#        graph[v1].append(v2) 

def delete_node(v): # directed or undirected and unweighted graph
    if v not in graph:
        print(v,'is not present')
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)
       
# def delete_node(v): # undirected or direceted and weighted graph
#     if v not in graph:
#         print(v,'is not present')
#     else:
#         graph.pop(v)
#         for i in graph:
#             list1 = graph[i]
#             for j in list1:
#                 if v == j[0]:
#                     list1.remove(j)
#                     break

def delete_edge(v1,v2): # undirected and unweighted graph
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

# def delete_edge(v1,v2): # directed and unweighted graph
#     if v1 not in graph:
#         print(v1,'is not present')
#     elif v2 not in graph:
#         print(v2,'is not present')
#     else:
#         if v2 in graph[v1]:
#             graph[v1].remove(v2)

# def delete_edge(v1,v2,cost): # undirected and weighted graph
#     if v1 not in graph:
#         print(v1,'is not present')
#     elif v2 not in graph:
#         print(v2,'is not present')
#     else:
#         temp1 = [v1,cost]
#         temp2 = [v2,cost]
#         if temp2 in graph[v1]:
#             graph[v1].remove(temp2)
#             graph[v2].remove(temp1)
                
def delete_edge(v1,v2,cost): # directed and weighted graph
    if v1 not in graph:
        print(v1,'is not present')
    elif v2 not in graph:
        print(v2,'is not present')
    else:
        temp = [v2,cost]
        if temp in graph[v1]:
            graph[v1].remove(temp)

# def DFS(node, visited, graph): # recursive approch
#     if node not in graph:
#         print('node is not present')
#         return
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for i in graph[node]:
#             DFS(i,visited,graph)
# visited = set()

def DFS(node,graph): # itertive approch
    visited = set()
    if node not in graph:
        print('node is not present')
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge('A','B')
add_edge('B','E')
add_edge('A','C')
add_edge('A','D')
add_edge('B','D')
add_edge('C','D')
add_edge('E','D')
print(graph)
DFS('A',graph)