import MapReduce
import sys

"""
MATRIX MULTIPLY
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

K = 5 # Matrix dimension
L = 5

def mapper(record):
    # key: document identifier
    # value: document contents
	key = record[0]
	value = record[3]
	if key == "a":
		i = record[1]
		j = record[2]
		for k in range(0,K):
			mr.emit_intermediate((i,k), (j,value))
	else:
		j = record[1]
		k = record[2]
		for i in range(0,L):
			mr.emit_intermediate((i,k), (j,value))

    

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
	mat = {}
	for entry in list_of_values:
		identifier = entry[0]
		if identifier in mat:
			mat[identifier] += [entry[1]]
		else:
			mat[identifier] = [entry[1]]

	result = 0
	for entry in mat:
		valist = mat[entry]
		if len(valist) != 1:
			result += valist[0]*valist[1]

	mr.emit((key[0],key[1],result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
