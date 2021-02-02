'''
https://www.codeeval.com/open_challenges/152/
'''
import sys

def main():
	with open(sys.argv[1],'r') as word_file:
		for line in word_file.readlines():
			age = int(line.strip())
			if age in xrange(3):
				print "Still in Mama's arms"
			elif age in xrange(3,5):
				print "Preschool Maniac" 
			elif age in xrange(5,12):
				print "Elementary school"
			elif age in xrange(12,15):
				print "Middle school"
			elif age in xrange(15,19):
				print "High school"
			elif age in xrange(19,23):
				print "College"
			elif age in xrange(23,66):
				print "Working for the man"
			elif age in xrange(66,101):
				print "The Golden Years"
			else:
				print "This program is for humans"

if __name__ == '__main__':
    main()