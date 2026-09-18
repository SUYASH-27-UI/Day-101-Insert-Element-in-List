numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

position = int(input("Enter index: "))
value = int(input("Enter value: "))

numbers.insert(position, value)

print("Updated list:", numbers)
