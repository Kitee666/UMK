import sys

if len(sys.argv) != 2:
    print("Usage: to_matrix.py <graph.txt>", file=sys.stderr)
    exit(-1)
nodeDict = {}
edgeDict = {}

for lines in open(sys.argv[1], 'r').readlines():
    node, edges = lines.strip().split(';')
    edges = edges.strip().split(',')
    if node not in nodeDict:
        nodeDict[node] = {}
    for i in edges:
        if i not in nodeDict:
            nodeDict[i] = {}

    print(node, edges)
    # nodes.append(int(val[0]))
    # for edge in val[1].strip().split(','):
    #     edges.append((int(edge), int(val[0])))