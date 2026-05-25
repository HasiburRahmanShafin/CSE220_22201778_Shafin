# problems.py: Extra practice, Mid, Final, and Hashing examples

import numpy as np
import math

# ---------- PRAC Section ----------
# Matrix compression (2x2 block sum) - repeated, but included for completeness
def compress_matrix(mat):
    row, col = mat.shape
    compressed = np.zeros((row//2, col//2), dtype=int)
    for i in range(0, row, 2):
        for j in range(0, col, 2):
            compressed[i//2][j//2] = mat[i][j] + mat[i+1][j] + mat[i][j+1] + mat[i+1][j+1]
    return compressed

# Walk zigzag (alternate version)
def walk_zigzag(floor):
    row, col = floor.shape
    for i in range(col):
        if i % 2 == 0:
            for j in range(0, row, 2):
                print(floor[j][i], end=" ")
        else:
            for j in range(row-1 if row%2==0 else row-2, -1, -2):
                print(floor[j][i], end=" ")
        print()

# Row rotation (alternative)
def row_rotation(exam_week, seat_status):
    row, col = seat_status.shape
    for _ in range(exam_week-1):
        last_row = seat_status[row-1].copy()
        for i in range(row-2, -1, -1):
            seat_status[i+1] = seat_status[i]
        seat_status[0] = last_row
    # Return seat status after rotation (not row of AA)
    return seat_status

# Reverse matrix (mirror both axes)
def reverse_Matrix(matrix):
    row, col = matrix.shape
    for i in range(row//2):
        for j in range(col):
            matrix[i][j], matrix[row-1-i][col-1-j] = matrix[row-1-i][col-1-j], matrix[i][j]
    if row % 2 == 1:
        mid = row // 2
        for j in range(col//2):
            matrix[mid][j], matrix[mid][col-1-j] = matrix[mid][col-1-j], matrix[mid][j]
    return matrix

# Knight moves (without bounds check, simplified)
def show_knight_move(knight):
    board = np.zeros((8,8), dtype=int)
    x, y = knight
    board[x][y] = 66
    moves = [(-2,1), (-2,-1), (2,1), (2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            board[nx][ny] = 3
    return board

# ---------- Mid Exam ----------
class MidExam:
    def __init__(self):
        self.length = 0
        self.arr = None

    def Length(self, header):
        cur = header
        while cur:
            self.length += 1
            cur = cur.next

    def Half_Half(self, header):
        self.arr = np.zeros(int((self.length+1)/2), dtype=object)
        if len(self.arr) == self.length/2:
            self.arr = np.zeros(len(self.arr)+1, dtype=object)
        cur = header
        for i in range(self.length//2):
            self.arr[i] = cur.elem
            cur = cur.next
        abc = Node(cur.elem, None)
        newadd = abc
        cur = cur.next
        while cur:
            new = Node(cur.elem, None)
            cur = cur.next
            newadd.next = new
            new.prev = newadd
            newadd = newadd.next
        self.arr[i+1] = abc

    def printAll(self):
        for i in range(len(self.arr)-1):
            print(self.arr[i], end=" ")
        cur = self.arr[i+1]
        while cur:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

# ---------- Final Exam ----------
# Sum of nodes at given distances (recursive version)
def sum_dist(LL, dis):
    if not dis:
        return 0
    return helper(LL, dis[0]) + sum_dist(LL, dis[1:])

def helper(LL, n, m=0):
    if LL is None:
        return 0
    if m == n:
        return LL.elem
    return helper(LL.next, n, m+1)

# Remove from hash table (helper)
def remove(hashTable, key):
    ind = (key + 3) % len(hashTable)  # assuming hash function
    head = hashTable[ind]
    if head and head.key == key:
        hashTable[ind] = head.next
    else:
        temp = head
        while temp and temp.next:
            if temp.next.key == key:
                temp.next = temp.next.next
                break
            temp = temp.next

# Swap children at levels < M (recursive)
def swap_child(root, level, M):
    if root is None:
        return
    if level < M:
        root.left, root.right = root.right, root.left
    swap_child(root.left, level+1, M)
    swap_child(root.right, level+1, M)
    return root

# ---------- Hashing Section ----------
class NodeHash:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class HashTableExample:
    def __init__(self, size):
        self.hashtable = np.array([None] * size)

    def hashFun(self, key):
        total = 0
        for i in range(len(key)):
            if i % 2 == 1:
                total += ord(key[i])
        return total % len(self.hashtable)

    def insert(self, key_val):
        idx = self.hashFun(key_val[0])
        node = NodeHash(key_val)
        if self.hashtable[idx] is None:
            self.hashtable[idx] = node
        else:
            node.next = self.hashtable[idx]
            self.hashtable[idx] = node

    def printLL(self, head):
        cur = head
        while cur:
            print(cur.val, end="-->")
            cur = cur.next
        return ""

    def printHashtable(self):
        for i in range(len(self.hashtable)):
            print(f"index: {i}")
            print(self.printLL(self.hashtable[i]))
            print()

# Example usage (commented)
# ht = HashTableExample(6)
# ht.insert(("shafin",1))
# ht.insert(("ilham",2))
# ht.printHashtable()
