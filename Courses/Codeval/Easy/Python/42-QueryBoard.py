'''
https://www.codeeval.com/open_challenges/87/
'''
import sys

def setRow(Matrix,row,value):
	for i in xrange(256):
		Matrix[row][i] = value

def setCol(Matrix,col,value):
	for i in xrange(256):
		Matrix[i][col] = value

def queryCol(Matrix,col):
	val = []
	for i in xrange(256):
		val.append(Matrix[i][col])
	print sum(val)

def queryRow(Matrix,row):
	val = []
	for i in xrange(256):
		val.append(Matrix[row][i])
	print sum(val)

def main():
	with open(sys.argv[1],'r') as word_file:
		Matrix = [[0 for x in xrange(256)] for x in xrange(256)] 
		for line in word_file.readlines():
			line = line.strip().split()
			command = line[0]
			if command == "SetRow":
				cvalue, value = int(line[1]),int(line[2])
				setRow(Matrix,cvalue,value)
			elif command == "SetCol":
				cvalue, value = int(line[1]),int(line[2])
				setCol(Matrix,cvalue,value)
			elif command == "QueryCol":
				col = int(line[1])
				queryCol(Matrix,col)
			else:
				row = int(line[1])
				queryRow(Matrix,row)




if __name__ == '__main__':
    main()