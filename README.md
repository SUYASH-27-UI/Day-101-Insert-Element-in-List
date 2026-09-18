# Day-101-Insert-Element-in-List
# Python Day 101 - Insert Element in List

This program inserts a new element at a specific index position in a list.

## Example

Original List:

```text
[10, 20, 30, 40, 50]
```

Input:

```text
Enter index: 2
Enter value: 100
```

Output:

```text
Updated list: [10, 20, 100, 30, 40, 50]
```

## Concepts Used

* Lists
* Indexing
* `input()`
* `int()`
* `insert()` method
* Variables

## How It Works

1. Create a list of numbers.
2. Display the original list.
3. Ask the user for the index position.
4. Ask the user for the new value.
5. Use the `insert()` method to add the value at that position.
6. Display the updated list.

## Python Code

```python
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

position = int(input("Enter index: "))
value = int(input("Enter value: "))

numbers.insert(position, value)

print("Updated list:", numbers)
```

## Output

```text
Original list: [10, 20, 30, 40, 50]
Enter index: 2
Enter value: 100
Updated list: [10, 20, 100, 30, 40, 50]
```

## Goal

The goal of this project is to practice Python lists, indexing, user input, and the `insert()` method.
