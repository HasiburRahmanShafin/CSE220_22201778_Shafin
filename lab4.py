# LAB 4: Doubly Linked List (WRM) and Stack Applications

class Node:
    def __init__(self, elem, next=None, prev=None):
        self.elem = elem
        self.next = next
        self.prev = prev

# ---------- Doubly Linked List for Patient Management ----------
class Patient:
    def __init__(self, pid, name, age, bg, next=None, prev=None):
        self.id = pid
        self.name = name
        self.age = age
        self.bg = bg
        self.next = next
        self.prev = prev

class WRM:
    def __init__(self):
        self.head = Patient(None, None, None, None)
        self.head.next = self.head
        self.head.prev = self.head

    def registerPatient(self, pid, name, age, bg):
        new = Patient(pid, name, age, bg, self.head, self.head.prev)
        self.head.prev.next = new
        self.head.prev = new
        print("\nPatient successfully registered")

    def servePatient(self):
        if self.head.next.id is None:
            print("\nNo patients to be served")
        else:
            print(f"\n{self.head.next.name} is served")
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

    def showAllPatient(self):
        temp = self.head.next
        if temp.id is None:
            print("No patients waiting, nothing to show.")
        else:
            print("\nShowing all patients:")
            while temp.id is not None:
                print(temp.name, end=' ' if temp.next.id else '\n')
                temp = temp.next

    def canDoctorGoHome(self):
        if self.head.next.id is None:
            print("\nCan doctor go home?\n-Yes, there isn't any patient.")
        else:
            print("\nCan doctor go home?\n-No, there are more patients.")

    def cancelAll(self):
        self.head.next = self.head
        self.head.prev = self.head
        print("\nAll appointments cancelled")

    def ReverseTheLine(self):
        if self.head.next.id is None:
            print("No patients waiting, nothing to reverse.")
        else:
            # Reverse the doubly linked list
            cur = self.head.next
            last = self.head.prev
            while cur != self.head:
                cur.prev, cur.next = cur.next, cur.prev
                cur = cur.prev
            # Swap head.next and head.prev
            self.head.next, self.head.prev = self.head.prev, self.head.next
            print("Waiting Line has been reversed")

# ---------- Stack (Linked List based) ----------
class Stack:
    def __init__(self):
        self.__top = None

    def push(self, elem):
        self.__top = Node(elem, self.__top)

    def pop(self):
        if self.__top is None:
            return None
        val = self.__top.elem
        self.__top = self.__top.next
        return val

    def peek(self):
        return self.__top.elem if self.__top else None

    def isEmpty(self):
        return self.__top is None

# Helper to print stack (recursive)
def print_stack(st):
    if st.isEmpty():
        return
    p = st.pop()
    print(f'| {p} |')
    print_stack(st)
    st.push(p)

# Task 1: Diamond Count (count matching <>)
def diamond_count(stack, string):
    count = 0
    for ch in string:
        if ch == '<':
            stack.push(ch)
        elif ch == '>' and not stack.isEmpty():
            stack.pop()
            count += 1
    return count

# Task 2: Remove block from stack (remove n-th from top)
def remove_block(stack, n):
    if n == 0:
        return stack
    temp_stack = Stack()
    for _ in range(n-1):
        if stack.isEmpty():
            break
        temp_stack.push(stack.pop())
    # Remove the target
    stack.pop()
    # Restore
    while not temp_stack.isEmpty():
        stack.push(temp_stack.pop())
    return stack

# Task 3: Conditional Reverse (remove consecutive duplicates)
def conditional_reverse(stack):
    new_stack = Stack()
    if stack.isEmpty():
        return new_stack
    new_stack.push(stack.pop())
    while not stack.isEmpty():
        val = stack.pop()
        if val != new_stack.peek():
            new_stack.push(val)
    return new_stack
