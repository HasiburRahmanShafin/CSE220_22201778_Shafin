# LAB 5: Recursive Functions

import numpy as np
import math

# Helper for linked list creation
class Node:
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

def create_linked_list(arr):
    head = Node(arr[0])
    tail = head
    for i in arr[1:]:
        tail.next = Node(i)
        tail = tail.next
    return head

# a) Sum of even positive elements in array (recursive)
def recursive_sum(arr, idx=0):
    if idx == len(arr):
        return 0
    if arr[idx] > 0 and arr[idx] % 2 == 0:
        return arr[idx] + recursive_sum(arr, idx+1)
    return recursive_sum(arr, idx+1)

# b) Product of odd positive elements in linked list (recursive)
def recursive_multiply(head):
    if head is None:
        return 1
    if head.elem > 0 and head.elem % 2 == 1:
        return head.elem * recursive_multiply(head.next)
    return recursive_multiply(head.next)

# c) nCr using recursive factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

# d) Count digits recursively
def count_digit_recursive(num):
    if num // 10 == 0:
        return 1
    return 1 + count_digit_recursive(num // 10)

# e) Check prime recursively
def check_prime_recursive(num, i=2):
    if i == num:
        return True
    if num % i == 0:
        return False
    return check_prime_recursive(num, i+1)

# f) Print linked list in reverse recursively
def recursive_print(head):
    if head is None:
        return
    recursive_print(head.next)
    print(head.elem)

# a) Decimal to binary recursively
def dec_to_binary_recursive(n):
    if n == 0:
        return ""
    return dec_to_binary_recursive(n // 2) + str(n % 2)

# b) Decimal to hexadecimal recursively
def encoding(dec_number):
    return '0123456789ABCDEF'[dec_number]

def dec_to_hexa_recursive(n):
    if n == 0:
        return ""
    return dec_to_hexa_recursive(n // 16) + encoding(n % 16)

# c) Print vowels then consonants recursively
def print_alphabets_recursive(head):
    if head is None:
        return
    if head.elem in "aeiouAEIOU":
        print(head.elem, end=" ")
    print_alphabets_recursive(head.next)
    if head.elem not in "aeiouAEIOU":
        print(head.elem, end=" ")

# d) Harmonic sum (alternating signs)
def harmonic_sum(n):
    if n == 1:
        return 1
    return ((-1)**(n+1))/n + harmonic_sum(n-1)

# a) House of Cards (HOC Builder)
def hoc_Builder(height):
    if height == 0:
        return 0
    if height == 1:
        return 8 + hoc_Builder(height-1)
    return 5 + hoc_Builder(height-1)

# b) Reach goal (Collatz steps)
def reach_goal(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + reach_goal(n // 2)
    else:
        return 1 + reach_goal(3*n + 1)

# a) Print pattern (n, n-5, ..., then back)
def print_pattern(n, spaces=0):
    if n <= 0:
        return
    print(" " * spaces, end="")
    _print_line(n)
    print()
    print_pattern(n-5, spaces + 1 + len(str(n)))

def _print_line(n):
    if n <= 0:
        print(n, end=" ")
        return
    print(n, end=" ")
    _print_line(n-5)
    print(n, end=" ")

# b) Merge two sorted lists into descending order (recursive)
def merge_Lists(mid, final, combined):
    if not mid and not final:
        return combined
    if not mid:
        combined = _insert_desc(combined, final[0])
    elif not final:
        combined = _insert_desc(combined, mid[0])
    else:
        combined = _insert_desc(combined, mid[0])
        combined = _insert_desc(combined, final[0])
    return merge_Lists(mid[1:], final[1:], combined)

def _insert_desc(lst, val):
    i = 0
    while i < len(lst) and lst[i] > val:
        i += 1
    lst.insert(i, val)
    return lst

# Flatten nested list (recursive)
def flatten_List(given_list, output):
    for item in given_list:
        if isinstance(item, list):
            flatten_List(item, output)
        else:
            output.append(item)
    return output

# Bonus: Number of ways to climb stairs (1,2,3 steps)
def number_of_ways(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return number_of_ways(n-1) + number_of_ways(n-2) + number_of_ways(n-3)
