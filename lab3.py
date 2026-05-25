# LAB 3: Singly Linked List Operations

class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

def createList(arr):
    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
        tail.next = Node(arr[i])
        tail = tail.next
    return head

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.elem, end='-->' if temp.next else '\n')
        temp = temp.next

# Task 1: Check if two linked lists are identical
def check_similar(building_1, building_2):
    cur1, cur2 = building_1, building_2
    while cur1 and cur2:
        if cur1.elem != cur2.elem:
            return "Not Similar"
        cur1, cur2 = cur1.next, cur2.next
    if cur1 is None and cur2 is None:
        return "Similar"
    return "Not Similar"

# Task 2: Remove n-th node from the end (1-indexed)
def remove_compartment(head, n):
    # Find length
    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next
    if n == length:
        return head.next
    if n > length:
        return head
    target = length - n
    cur = head
    for _ in range(target - 1):
        cur = cur.next
    cur.next = cur.next.next
    return head

# Task 3: Check if linked list is sorted in non-decreasing order
def assemble_conga_line(conga_line):
    cur = conga_line
    while cur and cur.next:
        if cur.elem > cur.next.elem:
            return False
        cur = cur.next
    return True

# Task 4: Word Decoder (extract every 13th character mod length)
def word_Decoder(head):
    # Find length
    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next
    step = 13 % length
    if step == 0:
        return Node(None)  # dummy head
    # Traverse and collect in reverse order
    values = []
    cur = head
    idx = 0
    while cur:
        if idx % step == 0:
            values.append(cur.elem)
        cur = cur.next
        idx += 1
    # Build reversed list
    dummy = Node(None)
    for v in reversed(values):
        new_node = Node(v, dummy.next)
        dummy.next = new_node
    return dummy

# Task 5: Alternate Merge
def alternate_merge(head1, head2):
    dummy = Node(None)
    tail = dummy
    cur1 = head1
    cur2 = head2
    turn = 0
    while cur1 and cur2:
        if turn == 0:
            tail.next = cur1
            cur1 = cur1.next
        else:
            tail.next = cur2
            cur2 = cur2.next
        tail = tail.next
        turn = 1 - turn
    if cur1:
        tail.next = cur1
    if cur2:
        tail.next = cur2
    return dummy.next

# Task 6: Sum of nodes at given indices
def sum_dist(head, indices):
    total = 0
    for idx in indices:
        cur = head
        count = 0
        while cur:
            if count == idx:
                total += cur.elem
                break
            cur = cur.next
            count += 1
    return total

# Bonus Task: ID Generator
def idGenerator(head1, head2, head3):
    # Reverse head1
    prev = None
    cur = head1
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    rev_head = prev
    # Build list from rev_head
    dummy = Node(None)
    tail = dummy
    cur1 = rev_head
    cur2 = head2
    cur3 = head3
    while cur1:
        tail.next = Node(cur1.elem)
        tail = tail.next
        cur1 = cur1.next
    while cur2 and cur3:
        s = cur2.elem + cur3.elem
        tail.next = Node(s % 10)
        tail = tail.next
        cur2 = cur2.next
        cur3 = cur3.next
    return dummy.next
