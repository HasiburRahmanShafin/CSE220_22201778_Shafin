# LAB 2: Matrix Operations

import numpy as np

def print_matrix(m):
    row, col = m.shape
    for i in range(row):
        print('|', end='')
        for j in range(col):
            print(f' {m[i][j]:2d} |', end='')
        print()
        print('-' * (col * 6 + 1))

# Task 1: Zigzag Walk
def walk_zigzag(floor):
    row, col = floor.shape
    for c in range(col):
        if c % 2 == 0:
            start = 0
            step = 2
            stop = row if row % 2 == 0 else row + 1
        else:
            start = row - 1 if row % 2 == 0 else row - 2
            step = -2
            stop = -1
        for r in range(start, stop, step):
            print(floor[r][c], end=' ')
        print()

# Task 2: Row Rotation Policy of BRACU Classroom
def row_rotation(exam_week, seat_status):
    row, col = seat_status.shape
    for _ in range(exam_week - 1):
        last_row = seat_status[row-1].copy()
        for i in range(row-2, -1, -1):
            seat_status[i+1] = seat_status[i]
        seat_status[0] = last_row
    # Find row of "AA"
    for i in range(row):
        if "AA" in seat_status[i]:
            return i+1
    return -1

# Task 3: Reverse Matrix (mirror both horizontally and vertically)
def reverse_Matrix(matrix):
    row, col = matrix.shape
    for i in range(row // 2):
        for j in range(col):
            matrix[i][j], matrix[row-1-i][col-1-j] = matrix[row-1-i][col-1-j], matrix[i][j]
    if row % 2 == 1:
        mid = row // 2
        for j in range(col // 2):
            matrix[mid][j], matrix[mid][col-1-j] = matrix[mid][col-1-j], matrix[mid][j]
    return matrix

# Task 4: Chess Piece - Knight Moves
def show_knight_move(knight):
    board = np.zeros((8, 8), dtype=int)
    x, y = knight
    board[x][y] = 66
    moves = [(-2,1), (-2,-1), (2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            board[nx][ny] = 3
    return board

# Task 5: Matrix Compression (2x2 block sum)
def compress_matrix(mat):
    row, col = mat.shape
    compressed = np.zeros((row//2, col//2), dtype=int)
    for i in range(0, row, 2):
        for j in range(0, col, 2):
            compressed[i//2][j//2] = mat[i][j] + mat[i+1][j] + mat[i][j+1] + mat[i+1][j+1]
    return compressed

# Task 6: Game Arena - Count points
def play_game(arena):
    points = 0
    row, col = arena.shape
    for i in range(row):
        for j in range(col):
            if arena[i][j] != 0 and arena[i][j] % 50 == 0:
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < row and 0 <= nj < col and arena[ni][nj] == 2:
                        points += 1
    total = points * 2
    print(f"Points Gained: {total}.", end=" ")
    if total < 10:
        print("Your team is out.")
    else:
        print("Your team has survived the game.")

# Bonus Task: Check if secondary diagonal of matrix1 equals primary diagonal of matrix2
def check_diagonal(matrix1, matrix2):
    n = matrix1.shape[0]
    if matrix1.shape == matrix2.shape and n >= 3:
        for i in range(n):
            if matrix1[i][n-1-i] != matrix2[n-1-i][n-1-i]:
                print("No")
                return
        print("Yes")
    else:
        print("No")
