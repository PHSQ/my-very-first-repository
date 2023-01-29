#diferenças entre o pprint e print normal com com loop e col

from pprint import pprint
import os

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9],
          [10, 11, 12]]

from pprint import pprint
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pprint(matrix)

os.system('clear')
#for y in range(len(matrix)):
#    print(" ".join([str(col[y]) for col in matrix]))

pprint(matrix)