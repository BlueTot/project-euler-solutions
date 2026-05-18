size = 1001
lst = [[0 for _ in range(size)] for _ in range(size)]
centre = (size + 1) // 2 - 1
lst[centre][centre] = 1
row, col = centre, centre
layer = 0
count = 1

try:

    while True:
        if ((size-1)-row) == col:
            col += 1
            count += 1
            lst[row][col] = count
            layer += 1
            
        else:

            while row < centre + layer:
                row += 1
                count += 1
                lst[row][col] = count
                
            while col > centre - layer:
                col -= 1
                count += 1
                lst[row][col] = count
                
            while row > centre - layer:
                row -= 1
                count += 1
                lst[row][col] = count
                
            while col < centre + layer:
                col += 1
                count += 1
                lst[row][col] = count
                
        # print(row, col)
        # print(lst)

except IndexError:
    for row in lst:
        for char in row:
            print(char, end=' ')
        print()
    total = 0
    for i in range(size):
        total += lst[i][i]
        if (size-1)-i != i:
            total += lst[(size-1)-i][i]
    print(total)
    # print(lst)