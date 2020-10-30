from terminaltables import SingleTable

queens = [-1, -1, -1, -1, -1, -1, -1, -1]
cols = [0, 0, 0, 0, 0, 0, 0, 0]
dc1 = {
    -7: 0,
    -6: 0,
    -5: 0,
    -4: 0,
    -3: 0,
    -2: 0,
    -1: 0,
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0
}
dc2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

count = 0
def print_result():
    global count
    count = count + 1
    data = []
    for i in range(0, 8):
        row = []
        for j in range(0, 8):
            if queens[i] == j:
                row.append("W")
            else:
                row.append(" ")
        data.append(row)
    table = SingleTable(data)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    
    print(table.table)

def is_available(x, y):
    if cols[y] != 0:
        return False
        
    if dc1[x - y] != 0:
        return False

    if dc2[x + y] != 0:
        return False

    return True

def put_queens(x, y):
    cols[y] = 1
    queens[x] = y
    dc1[x-y] = 1
    dc2[x+y] = 1

def remove_queen(x, y):
    cols[y] = 0
    queens[x] = -1
    dc1[x-y] = 0
    dc2[x+y] = 0

def solve():
    for w0 in range(0, 8):
        if is_available(0, w0):
            put_queens(0, w0)
            for w1 in range(0, 8):
                if is_available(1, w1):
                    put_queens(1, w1)
                    for w2 in range(0, 8):
                        if is_available(2, w2):
                            put_queens(2, w2)
                            for w3 in range(0, 8):
                                if is_available(3, w3):
                                    put_queens(3, w3)
                                    for w4 in range(0, 8):
                                        if is_available(4, w4):
                                            put_queens(4, w4)
                                            for w5 in range(0, 8):
                                                if is_available(5, w5):
                                                    put_queens(5, w5)
                                                    for w6 in range(0, 8):
                                                        if is_available(6, w6):
                                                            put_queens(6, w6)
                                                            for w7 in range(0, 8):
                                                                if is_available(7, w7):
                                                                    put_queens(7, w7)
                                                                    print_result()
                                                                    remove_queen(7, w7)
                                                            remove_queen(6, w6)    
                                                    remove_queen(5, w5)
                                            remove_queen(4, w4)
                                    remove_queen(3, w3)
                            remove_queen(2, w2)
                    remove_queen(1, w1)
            remove_queen(0, w0)

solve()
print(count);
