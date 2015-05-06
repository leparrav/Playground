    data = open('file.csv', 'r')

    row_index = 1
    for line in data:
        row = [int(each) for each in line.split()]
        max_number = max(row)
        colmax_index = [i for i, j in enumerate(row) if j == max_number]
        if len(colmax_index) == 1:
            print row_index, colmax_index[0]+1 # Remember 0 - Count
        row_index += 1

    data.close()