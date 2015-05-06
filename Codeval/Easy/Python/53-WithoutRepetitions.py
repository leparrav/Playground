import sys

def main():
    with open(sys.argv[1],'r') as word_file:
        for line in word_file.readlines():
            line = line.strip().split()
            clean_line = []
            for word in line:
                clean_word, index, last_letter = "",0,None
                for letter in word:
                    if letter != last_letter:
                        clean_word += letter
                        last_letter = letter
                clean_line.append(clean_word)
            print " ".join(clean_line)
            
if __name__ == '__main__':
    main()