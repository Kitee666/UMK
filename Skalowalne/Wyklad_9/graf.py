def show(keys, values):
    for k in keys:
        print(k, ' -> ', values[k])


graf = open('graf.txt', 'r').readlines()

vert = {}
edges = []

for i in graf:
    line = i.split()
    a, b = int(line[0]), int(line[1])
    vert[a] = a
    vert[b] = b
    edges.append([a, b])

# Wierzcholki
graf_vert = list(vert.keys())
# Lista sasiedztwa
graf_edges = {}
# Krok niebieski
graf_connect = {}
for i in vert:
    graf_edges[i] = []
    graf_connect[i] = i
for i in edges:
    a, b = i
    graf_edges[a].append(b)
    graf_edges[b].append(a)
print("Krok niebieski")
show(graf_vert, graf_connect)

# Krok zielony

copy_connect = graf_connect.copy()
for v in vert:
    neigh = [copy_connect[i] for i in graf_edges[v]]
    x = min(neigh)
    if x < graf_connect[v]:
        graf_connect[v] = x
print("Krok zielony")
show(graf_vert, graf_connect)

# Krok pomaranczowy
copy_connect = graf_connect.copy()
for v in vert:
    graf_connect[v] = copy_connect[copy_connect[v]]

print("Krok pomaranczowy")
show(graf_vert, graf_connect)

# Krok zielony
copy_connect = graf_connect.copy()
for v in vert:
    neigh = [copy_connect[i] for i in graf_edges[v]]
    x = min(neigh)
    if x < graf_connect[v]:
        graf_connect[v] = x
print("Krok zielony 2")
show(graf_vert, graf_connect)

# Krok pomaranczowy
copy_connect = graf_connect.copy()
for v in vert:
    graf_connect[v] = copy_connect[copy_connect[v]]

print("Krok pomaranczowy 2")
show(graf_vert, graf_connect)
