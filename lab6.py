# LAB 6: Hash Tables with Chaining

import numpy as np

# ---------- Task 1: Vehicle Hash Table ----------
class vehicleNodes:
    def __init__(self, brand, vehicle_type, rent, passenger, next=None):
        self.brand = brand
        self.vehicle_type = vehicle_type
        self.rent = rent
        self.passenger = passenger
        self.next = next

class VehicleHashTable:
    def __init__(self, size):
        self.vehicleTable = [None] * size
        self.empty_slot = {i: False for i in range(size)}

    def __hash_function(self, brand):
        if brand == "":
            return 0
        total = 0
        for ch in brand:
            total += ord(ch)
        idx = total % len(self.vehicleTable)
        if idx in self.empty_slot:
            del self.empty_slot[idx]
        return idx

    def insert_vehicle(self, vehicle):
        node = vehicleNodes(vehicle[0], vehicle[1], vehicle[2], vehicle[3])
        idx = self.__hash_function(node.brand)
        if self.vehicleTable[idx] is None:
            self.vehicleTable[idx] = node
        else:
            # Insert at head (chaining)
            node.next = self.vehicleTable[idx]
            self.vehicleTable[idx] = node

    def create_from_vehicle_info_array(self, arr):
        for v in arr:
            self.insert_vehicle(v)

    def print_vehicle_hashtable(self):
        for idx, head in enumerate(self.vehicleTable):
            print(idx, ':', end=' ')
            temp = head
            while temp:
                print(f"(Brand: {temp.brand}, Type: {temp.vehicle_type}, Rent: {temp.rent}, No. of Passengers: {temp.passenger})", end='---->')
                temp = temp.next
            print('None')
            print()

# ---------- Task 2: Hash Table with key-value pairs ----------
class Node_pair:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class Hashtable:
    def __init__(self, size):
        self.ht = [None] * size

    def __hash_function(self, key):
        if len(key) == 0:
            return 0
        if len(key) == 1:
            key += "N"
        total = 0
        for i in range(0, len(key), 2):
            if i+1 < len(key):
                total += int(str(ord(key[i])) + str(ord(key[i+1])))
            else:
                total += ord(key[i])
        return total % len(self.ht)

    def insert(self, s):
        if self.search_hashtable(s) == 'Found':
            print(s, 'Already Inserted. Cannot reinsert.')
            return
        idx = self.__hash_function(s[0])
        pair = Node_pair(s[0], s[1])
        if self.ht[idx] is None:
            self.ht[idx] = pair
        else:
            pair.next = self.ht[idx]
            self.ht[idx] = pair

    def create_from_array(self, arr):
        for i in arr:
            self.insert(i)

    def print_hashtable(self):
        for idx, head in enumerate(self.ht):
            print(idx, ':', end=' ')
            temp = head
            while temp:
                print(f'({temp.key}, {temp.value})', end='-->')
                temp = temp.next
            print('None')
            print()

    def search_hashtable(self, s):
        idx = self.__hash_function(s[0])
        temp = self.ht[idx]
        while temp:
            if temp.key == s[0] and temp.value == s[1]:
                return 'Found'
            temp = temp.next
        return 'Not Found'

# ---------- Task 3: Hash Table with sorted chains by value ----------
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class HashTable:
    def __init__(self, length):
        self.ht = [Node() for _ in range(length)]
        self.length = length

    def __hash_function(self, key):
        if len(key) == 0:
            return 0
        if len(key) % 2 != 0:
            return self.__hash_function(key[1:])
        total = ord(key[0]) + self.__hash_function(key[2:])
        return total % self.length

    def insert(self, key, value):
        node = Node((key, value))
        idx = self.__hash_function(key)
        head = self.ht[idx]
        if head.value is None:
            self.ht[idx] = node
        else:
            # Insert in decreasing order of value
            if head.value[1] < node.value[1]:
                node.next = head
                self.ht[idx] = node
            else:
                temp = head
                while temp.next and temp.next.value[1] >= node.value[1]:
                    temp = temp.next
                node.next = temp.next
                temp.next = node

    def show(self):
        for idx, head in enumerate(self.ht):
            temp = head
            print(idx, end=' ')
            while temp and temp.value:
                print(temp.value, end='-->')
                temp = temp.next
            print()

# ---------- Task 4: Hash Table with remove method ----------
class Node_pair_remove:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashtableRemove:
    def __init__(self, size):
        self.ht = [None] * size

    def __hash_function(self, key):
        return (key + 3) % len(self.ht)

    def insert(self, s):
        idx = self.__hash_function(s[0])
        pair = Node_pair_remove(s[0], s[1])
        if self.ht[idx] is None:
            self.ht[idx] = pair
        else:
            pair.next = self.ht[idx]
            self.ht[idx] = pair

    def create_from_array(self, arr):
        for i in arr:
            self.insert(i)

    def print_hashtable(self):
        for idx, head in enumerate(self.ht):
            print(idx, ':', end=' ')
            temp = head
            while temp:
                print(f'({temp.key}, {temp.value})', end='-->')
                temp = temp.next
            print('None')

    def remove(self, key):
        idx = self.__hash_function(key)
        head = self.ht[idx]
        if head is None:
            return
        if head.key == key:
            self.ht[idx] = head.next
            return
        prev = head
        cur = head.next
        while cur:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
