# Enter your code here. Read input from STDIN. Print output to STDOUT

n_s, m_s = input().split(" ")
n = int(n_s)
m = int(m_s)

roads = {}
current_node = None
path = []
result = ""

for i in range(m):

    a_s, b_s = input().split(" ")
    a = int(a_s)
    b = int(b_s)

    if current_node == None:
        current_node = b

    if a in roads:
        roads[a].append(b)
    else:
        roads[a] = [b]
    if b in roads:
        roads[b].append(a)
    else:
        roads[b] = [a]

def get_available_nodes(n, roads, path):
    if n not in roads:
        return []
    
    return list(filter(lambda x: x not in path, roads[n]))

while current_node != None:
    
    available_nodes = get_available_nodes(current_node, roads, path)
    if available_nodes == []:
        break
    
    next_node = available_nodes[0]
    path.append(next_node)
    result += str(next_node) + " "
    current_node = next_node

print(len(path))
print(result)
