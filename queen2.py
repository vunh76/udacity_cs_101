from terminaltables import SingleTable

chess_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

count = 0
def print_result():
    global count
    count = count + 1
    data = []
    for i in range(0, 8):
        row = []
        for j in range(0, 8):
            if chess_board[i][j] != 0:
                row.append("W")
            else:
                row.append(" ")
        data.append(row)
    table = SingleTable(data)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    
    print(table.table)

def is_available(x, y):
    for i in range(0, 8):
        if chess_board[i][y] != 0:
            return False
        if chess_board[x][i] != 0:
            return False
        
    row = x
    col = y
    while True:
        row = row + 1
        col = col + 1
        if row == 8 or col == 8:
            break
        if chess_board[row][col] != 0:
            return False
    row = x
    col = y
    while True:
        row = row - 1
        col = col - 1
        if row < 0 or col < 0:
            break
        if chess_board[row][col] != 0:
            return False

    row = x
    col = y
    while True:
        row = row - 1
        col = col + 1
        if row < 0 or col == 8:
            break
        if chess_board[row][col] != 0:
            return False

    row = x
    col = y
    while True:
        row = row + 1
        col = col - 1
        if row == 8 or col < 0:
            break
        if chess_board[row][col] != 0:
            return False

    return True

def solve():
    for w0 in range(0, 8):
        if is_available(0, w0):
            chess_board[0][w0] = 1
            for w1 in range(0, 8):
                if is_available(1, w1):
                    chess_board[1][w1] = 1
                    for w2 in range(0, 8):
                        if is_available(2, w2):
                            chess_board[2][w2] = 1
                            for w3 in range(0, 8):
                                if is_available(3, w3):
                                    chess_board[3][w3] = 1
                                    for w4 in range(0, 8):
                                        if is_available(4, w4):
                                            chess_board[4][w4] = 1
                                            for w5 in range(0, 8):
                                                if is_available(5, w5):
                                                    chess_board[5][w5] = 1
                                                    for w6 in range(0, 8):
                                                        if is_available(6, w6):
                                                            chess_board[6][w6] = 1
                                                            for w7 in range(0, 8):
                                                                if is_available(7, w7):
                                                                    chess_board[7][w7] = 1
                                                                    print_result()
                                                                    chess_board[7][w7] = 0
                                                            chess_board[6][w6] = 0    
                                                    chess_board[5][w5] = 0
                                            chess_board[4][w4] = 0
                                    chess_board[3][w3] = 0
                            chess_board[2][w2] = 0
                    chess_board[1][w1] = 0
            chess_board[0][w0] = 0

solve()
print(count);
