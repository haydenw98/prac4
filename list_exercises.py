numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average is {}".format((sum(numbers))/len(numbers)))
    user = input("Please enter username: ")
    if user in usernames:
        print("Access Granted")
    else:
        print("Access denied")

main()