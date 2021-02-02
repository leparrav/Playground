'''
Description: https://www.codeeval.com/open_challenges/41/
'''

import sys

def main():
    with open(sys.argv[1]) as word_file:
        for line in word_file.readlines():
            line = line.strip()
            N, numbers_string = line.split(';')
            N = int(N)
            numbers = [int(number) for number in numbers_string.split(',')]
            print sum(numbers)-(N-2)*(N-1)/2


if __name__ == '__main__':
    main()