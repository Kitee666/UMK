import sys

if len(sys.argv) != 2:
    print("Usage: List_to_matrix.py <graph.txt>", file=sys.stderr)
    exit(-1)
nodeDict = {}
edgeDict = {}

for lines in open(sys.argv[1], 'r').readlines():
    node, edges = lines.strip().split(';')
    edges = edges.strip().split(',')
    node = int(node)
    if node not in nodeDict:
        nodeDict[node] = {}
    for i in edges:
        i = int(i)
        nodeDict[node][i] = ''

for key, val in nodeDict.items():
    for val_key, _ in val.items():
        print(f'{val_key};{key};{1.0 / len(val)}')
