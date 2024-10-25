# zig zag convertion

def zigzagConvertion(list, rowsize):
    index = 0
    step = 1
    row = [[] for rows in range(rowsize)]
    for char in list:
        row[index].append(char)
        if index == 0:
            step = 1
        elif index == rowsize -1:
            step = -1
        index = index + step
    return row

    for i in range(rowsize):
        rows[i] = ''.join(rows[i])
    return ''.join(rows)

list = "hello there"
row = 3
print(zigzagConvertion(list,row))
