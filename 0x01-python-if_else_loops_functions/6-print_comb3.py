#!/usr/bin/python3
for num in range(100):
    if num !=89 and int(num / 10) != num % 10 and int(num / 10) < num % 10:
        print("{}{}, ".format(int(num / 10), num % 10), end="")
    if (num == 89):
        print(f"{num}")
