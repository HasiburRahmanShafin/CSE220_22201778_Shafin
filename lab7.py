# LAB 7: Binary Trees

class BTNode:
    def __init__(self, elem):
        self.elem = elem
        self.right = None
        self.left = None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.elem, end=' ')
        inorder(root.right)

def tree_construction(arr, i=1):
    if i >= len(arr) or arr[i] is None:
        return None
    p = BTNode(arr[i])
    p.left = tree_construction(arr, 2*i)
    p.right = tree_construction(arr, 2*i+1)
    return p

# Task 1: Mirror Tree
def convert_mirror(root):
    if root is None:
        return None
    new = BTNode(root.elem)
    new.left = convert_mirror(root.right)
    new.right = convert_mirror(root.left)
    return new

# Task 2: Smallest value at each level
def smallest_level(root, lvl=0, dic=None):
    if dic is None:
        dic = {}
    if root is None:
        return
    if lvl not in dic:
        dic[lvl] = root.elem
    elif dic[lvl] > root.elem:
        dic[lvl] = root.elem
    smallest_level(root.left, lvl+1, dic)
    smallest_level(root.right, lvl+1, dic)
    return dic

# Task 3: Inorder Predecessor (in BST)
def inorder_predecessor(root, x):
    # Predecessor is rightmost node of left subtree
    if x.left:
        cur = x.left
        while cur.right:
            cur = cur.right
        return cur
    return None

# Task 4: Lowest Common Ancestor (BST)
def LCA(root, x, y):
    if root is None:
        return None
    if root.elem == x or root.elem == y:
        return root.elem
    if (root.elem > x and root.elem < y) or (root.elem > y and root.elem < x):
        return root.elem
    if root.elem > x and root.elem > y:
        return LCA(root.left, x, y)
    return LCA(root.right, x, y)

# Task 5: Sum Tree (node value mod level)
def sumTree(root, lvl=0):
    if root is None:
        return 0
    if lvl == 0:
        return root.elem + sumTree(root.left, lvl+1) + sumTree(root.right, lvl+1)
    else:
        return (root.elem % lvl) + sumTree(root.left, lvl+1) + sumTree(root.right, lvl+1)

# Task 6: Swap children at levels < M
def swap_child(root, level, M):
    if root is None:
        return
    if level < M:
        root.left, root.right = root.right, root.left
    swap_child(root.left, level+1, M)
    swap_child(root.right, level+1, M)
    return root

# Task 7: Subtract sum of left subtree from right subtree
def subtract_summation(root):
    def sum_tree(node):
        if node is None:
            return 0
        return node.elem + sum_tree(node.left) + sum_tree(node.right)
    if root is None:
        return 0
    return sum_tree(root.left) - sum_tree(root.right)

# Bonus Task: Level sum with alternating signs
def level_sum(root, level=0):
    if root is None:
        return 0
    if level % 2 == 0:
        return -root.elem + level_sum(root.left, level+1) + level_sum(root.right, level+1)
    else:
        return root.elem + level_sum(root.left, level+1) + level_sum(root.right, level+1)
