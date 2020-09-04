numbers = [3, 1, 4, 1, 5, 9, 2]

def main():
    numbers.insert(0, "ten")
    numbers.append(1)
    print(numbers[2:])
    print(9 in numbers)
    print(numbers)
main()