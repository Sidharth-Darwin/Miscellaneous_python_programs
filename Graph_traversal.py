# Graph traversal - Breadth first search and Depth First search

def main()->None:
    nodes = int(input("Enter the no of nodes: "))
    adjacency_matrix = [[0 for i in range(nodes)] for j in range(nodes)]
    for index,col in enumerate(adjacency_matrix):
        edge_list = eval(input(f"Enter the outdegree nodes of {index}: "))
        col = [1 if i in edge_list else 0 for i in range(len(col))]
        adjacency_matrix[index] = col
    for index,value in enumerate(adjacency_matrix):
        print(index,value,sep='  ')
    while(True):
        source = int(input("Enter the source node: "))
        print("The result of Breadth first search: ")
        Bfs(nodes,source,adjacency_matrix)
        print("The result of Depth first search: ")
        Dfs(nodes,source,adjacency_matrix)
        
def Bfs(nodes,source,adjacency_matrix)->None:
    visited = set()
    queue = []
    queue.append(source)
    while (len(queue)>0):
        value = queue.pop(0)
        if value not in visited:
            visited.add(value)
            print(f"{value},",end=' ')
            for i in range(nodes):
                if (adjacency_matrix[value][i]==1):
                    if i not in visited:
                        queue.append(i)
    print("")
    
def Dfs(nodes,source,adjacency_matrix)->None:
    visited = set()
    stack = []
    stack.append(source)
    while (len(stack)>0):
        value = stack.pop()
        if value not in visited:
            visited.add(value)
            print(f"{value},",end=' ')
            for i in range(nodes):
                if (adjacency_matrix[value][i]==1):
                    if i not in visited:
                        stack.append(i)
    print("")
    
if __name__ == "__main__":
    main()
