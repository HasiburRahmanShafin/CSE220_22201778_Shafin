
---

## lab1.py (LAB 1: Arrays and Basic Functions)
```python
# LAB 1: Array Manipulation and Basic Functions

import numpy as np
import math

# Task 01: Merge Lineup
def mergeLineup(pokemon_1, pokemon_2):
    result = np.array([0] * len(pokemon_1))
    for i in range(len(pokemon_1)):
        a = pokemon_1[i] if pokemon_1[i] is not None else 0
        b = pokemon_2[len(pokemon_1)-i-1] if pokemon_2[len(pokemon_1)-i-1] is not None else 0
        result[i] = a + b
    return result

# Task 02: Discard Cards
def discardCards(cards, t):
    count = 0
    i = 0
    while i < len(cards):
        if cards[i] == t and count % 2 == 0:
            count += 1
            for j in range(i+1, len(cards)):
                cards[j-1] = cards[j]
            cards[len(cards)-1] = 0
            continue
        elif cards[i] == t and count % 2 != 0:
            count += 1
        i += 1
    return cards

# Task 03: DUBER Fare Splitting
def findGroups(money, fare):
    group = 0
    n = len(money)
    used = [False] * n
    for i in range(n):
        if used[i]:
            continue
        found = False
        for j in range(i+1, n):
            if not used[j] and money[i] + money[j] == fare:
                group += 1
                print(f"Group {group} : {money[i]}, {money[j]}")
                used[i] = used[j] = True
                found = True
                break
        if not found and not used[i] and money[i] == fare:
            group += 1
            print(f"Group {group} : {money[i]}")
            used[i] = True
    ungrouped = [money[k] for k in range(n) if not used[k]]
    if ungrouped:
        print("Ungrouped :", *ungrouped)

# Task 04: Get Those Hobbies
def analyzeHobbies(*participants):
    # Collect all unique hobbies
    all_hobbies = []
    for arr in participants:
        for h in arr:
            if h not in all_hobbies:
                all_hobbies.append(h)
    unique = np.array(all_hobbies)
    counts = np.zeros(len(unique), dtype=int)
    for i, h in enumerate(unique):
        for arr in participants:
            if h in arr:
                counts[i] += 1
    print("Unique Activities in the Town:")
    print(unique)
    print("\nStatistics:")
    for i in range(len(unique)):
        print(f"{counts[i]} participant(s) like(s) {unique[i]}.")

# Bonus Task: Look and Say
def look_and_say(arr):
    result = np.zeros(100, dtype=int)
    pos = 0
    i = 0
    while i < len(arr):
        count = 1
        j = i+1
        while j < len(arr) and arr[j] == arr[i]:
            count += 1
            j += 1
        result[pos] = count
        result[pos+1] = arr[i]
        pos += 2
        i = j
    return result

# Assignment Part-1: Mean, Standard Deviation, Outlier Removal
def mean(arr):
    return sum(arr) / len(arr)

def sd(arr):
    x_bar = mean(arr)
    total = sum((x - x_bar) ** 2 for x in arr)
    return round((total / (len(arr) - 1)) ** 0.5, 2)

def new_array(arr):
    x_bar = mean(arr)
    u = sd(arr)
    outliers = [x for x in arr if x < (x_bar - 1.5 * u) or x > (x_bar + 1.5 * u)]
    if not outliers:
        return None
    return np.array(outliers)

# Example usage (commented out)
# sample = np.array([10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4])
# print(f"The mean of the numbers is: {mean(sample)}")
# print(f"The standard deviation is: {sd(sample)}")
# print(f"New array: {new_array(sample)}")
