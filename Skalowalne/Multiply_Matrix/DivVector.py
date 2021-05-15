import sys
import math

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: DivMatrix.py vector.csv number_of_clusters output_file_name")
        exit(-1)

    rows = int(sys.argv[2])
    matrix = open(sys.argv[1], 'r')

    for line in matrix.readlines():
        r = int(line.strip().split(';')[0])
        open(sys.argv[3] + "_{}.csv".format(int(r // rows)), 'a+').write(line)
