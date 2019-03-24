import sys
def root(pq):
    return 0
def set_root(pq, c):
    if len(pq) != 0:
        pq[0] = c
def get_data(pq, p):
    return pq[p]
def parent(p):
    return (p - 1) // 2
def add_last(pq, c):
    pq.append(c)
def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]
def children(pq, p):
    if 2*p + 2 < len(pq):
        return [2*p + 1, 2*p + 2]
    else:
        return [2*p + 1]
def extract_last_from_pq(pq):
    return pq.pop()
def has_children(pq, p):
    return 2*p + 1 < len(pq)
def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        # Use the data stored at each child as the comparison key
        # for finding the minimum.
        j = min(children(pq, i), key=lambda x: get_data(pq, x))
        if get_data(pq, i) < get_data(pq, j):
            return c        
        exchange(pq, i, j)
        i = j
    return c
def insert_in_pq(pq, c):
    pq.append(c)
    i = len(pq) - 1
    while i != 0 and pq[i] < pq[(i - 1) // 2]:
        p = (i - 1) // 2
        pq [i], pq[p] = pq[p], pq[i]
        i = p
def look_above(pq,i):
    while i!=0 and pq[i] < pq[(i - 1) // 2]:
        #Checks if the node's value is lower than its parent
        #if so exchange the two nodes
        p = (i - 1) // 2
        pq [i], pq[p] = pq[p], pq[i]
        i = p
        
def search(pq,opn,i):
    while ():
        if opn == pq[i]:
            return i
        elif opn < pq[2*i+1]:
            return  search(pq,opn,2*i+2)
        elif opn < pq[2*i +2]:
            return search(pq,opn,2*i+1)
        else:
        

input_filename = "example_graph.txt"
#input_filename = sys.argv[1]
g = {}
with open(input_filename) as graph_input:
    for line in graph_input:
        # Split line and convert line parts to integers.
        nodes = [int(x) for x in line.split()]
        if len(nodes) != 2:
            continue
        # If a node is not already in the graph
        # we must create a new empty list.
        if nodes[0] not in g:
            g[nodes[0]] = []
        if nodes[1] not in g:
            g[nodes[1]] = []
        # We need to append the "to" node
        # to the existing list for the "from" node.
        g[nodes[0]].append(nodes[1])
        # And also the other way round.
        g[nodes[1]].append(nodes[0])
V = len(g)
mh = []
d = []
p = []
core = []
for v in range(V):#Declare lists as needed
    d.append(g[v])#List d is adjacency list
    p.append(len(d[v]))
    core.append(0)
    pn = [p[v], v] #icludes the v node and its number of neighbours
    insert_in_pq(mh,pn)
while len(mh) > 0:
    t = extract_min_from_pq(mh)
    core[t[1]] = t[0]
    if len(mh) != 0:
        for j in range(len(d[t[1]])): #loops until is surpasses all neighboors of the extracted node
            v = d[t[1]][j] #number of node,neighbour to the extracted one
            opn = [p[v],v]
            #for k in range(len(mh)): #finds the spot of the node in the list
                #if mh[k] == opn:
                    #break  
            k = search(mh,opn,0)
            print(k)
            break
            d[v].remove(t[1]) #removes from the adjacency list the extracted node
            p[v] = max(t[0],len(d[v]))
            npn = [p[v], v]
            mh[k] = npn #updates priority queue with the new value
            look_above(mh,k) #guarantees that the min heap still exists
for i in range(len(core)):
    print(i," ",core[i]) 
     