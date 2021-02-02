import MapReduce
import sys

"""
SQL JOIN
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  # key: document identifier
  # value: document contents

  key = (record[0],record[1])
  value = 1
  mr.emit_intermediate(key, value)

  #Reversed friendship
  key = (record[1],record[0])
  mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	if len(list_of_values) == 1:
		mr.emit((key[0],key[1]))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)