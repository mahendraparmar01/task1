while True:
    print("\n=== Basic Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "5":
        print("Thanks for using the calculator.")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Please enter a number between 1 and 5.")
        continue


    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except:
        print("Please enter valid numbers.")
        continue

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero.")
            continue
        result = num1 / num2

    print("Result is:", result)
