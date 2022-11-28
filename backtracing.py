def islegalboard(board):
    #horizontal and vertical checking
    for i in range(len(board)):
        seenH = []
        seenV = []
        for j in range(len(board)):
            if board[i][j] in seenH:
                return False
            else:
                if board[i][j] > 0:
                    seenH.append(board[i][j])
            if board[j][i] in seenV:
                return False
            else:
                if board[j][i] > 0:
                    seenV.append(board[j][i])
    #check box
    for rowB in range(3):
        for colB in range(3):
            seen = []
            for i in range(9):
                if board[(rowB* 3) + int(i/3)][(colB * 3) + i%3] in seen:
                    return False
                else:
                    if board[(rowB* 3) + int(i/3)][(colB * 3) + i%3] > 0:
                     seen.append(board[(rowB* 3) + int(i/3)][(colB * 3) + i%3])
    return True




sampleboard = [     [0, 7, 0, 0, 0, 2, 0, 0, 5],
                    [1, 0, 6, 0, 0, 0, 0, 0, 0],
                    [0, 8, 4, 0, 0, 0, 3, 6, 0],
                    [0, 0, 1, 0, 0, 8, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 9, 7, 0],
                    [0, 0, 0, 9, 7, 0, 0, 4, 0],
                    [0, 0, 0, 2, 0, 9, 4, 0, 8],
                    [3, 0, 0, 0, 6, 0, 0, 0, 9],
                    [0, 5, 0, 0, 0, 0, 0, 0, 0]]

for i in range(9):
    print(sampleboard[i])


print()
print()
#find already filled
filled = []
for i in range(9 ** 2):
    if sampleboard[int(i/9)][i % 9] != 0:
        filled.append(i)
for j in range(9 ** 2):
    if j not in filled:
        i = j
        break
while i < 9 ** 2:
    sampleboard[int(i/9)][i%9] = sampleboard[int(i/9)][i%9] + 1
    if islegalboard(sampleboard):
        i += 1
        while i in filled:
            i += 1
        if i >= 9 ** 2:
            break
    #in case of invalid path, go back
    while (sampleboard[int(i/9)][i%9] == 9 and i not in filled) or i in filled:
        if i not in filled:
            sampleboard[int(i/9)][i%9] = 0
        i -= 1


#print completed board
for i in range(9):
    print(sampleboard[i])