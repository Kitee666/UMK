import sys

if len(sys.argv) != 4:
    print("Usage: List_to_matrix.py <graph.txt> block_size output_name", file=sys.stderr)
    exit(-1)
nodeDict = {}
edgeDict = {}
size = int(sys.argv[2])

for lines in open(sys.argv[1], 'r').readlines():
    node, edges = lines.strip().split(';')
    edges = edges.strip().split(',')
    node = int(node)
    if node not in nodeDict:
        nodeDict[node] = {}
    for i in edges:
        i = int(i)
        nodeDict[node][i] = ''

blocks = {}
for key, val in nodeDict.items():
    for val_key, _ in val.items():
        row = int(key // size)
        col = int(val_key // size)

        if row not in blocks:
            blocks[row] = {}
        if col not in blocks[row]:
            blocks[row][col] = {}
        if key not in blocks[row][col]:
            blocks[row][col][key] = {}
        blocks[row][col][key][val_key] = ''

for key, val in blocks.items():
    for val_key, val_val in val.items():
        print("Block", key, val_key)
        file = open(sys.argv[3] + "_" + str(key) + "_" + str(val_key) + ".csv", "w+")
        out = ""
        for node_val_key, neigh_val_key in val_val.items():
            out += str(node_val_key) + ";" + str(len(nodeDict[node_val_key]))
            print(node_val_key, len(nodeDict[node_val_key]), end=" ")
            for key_node, _ in neigh_val_key.items():
                out += ";" + str(key_node)
                print(key_node, end=" ")
            print()
            out += "\n"
        file.write(out)
        file.close()
