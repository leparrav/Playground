'''
https://www.codeeval.com/open_challenges/23/
'''
def main():
	end = 12
	for i in xrange(1,end+1):
		numbers = [str(i*n).strip() for n in range(1,end+1)]
		format = " "*4
		first = True
		to_print = []
		for n in numbers:
			if first:
				to_print.append(format[2:-len(n)]+n)
				first= False
			else:
				to_print.append(format[0:-len(n)]+n)
		print "".join(to_print)


if __name__ == '__main__':
    main()