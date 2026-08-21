def add(a, b):
    pass


def subtract(a, b):
    pass


def multiply(a, b):
    pass


def divide(a, b):
    pass


def power(a, b):
    pass


def remainder(a, b):
    pass


def main():
    while True:
        print("\n--- Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Remainder")
        print("7. Exit")

        choice = input("Choose: ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice")
            continue

        a = float(input("First number: "))
        b = float(input("Second number: "))

        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
        elif choice == "5":
            print("Result:", power(a, b))
        elif choice == "6":
            print("Result:", remainder(a, b))


if __name__ == "__main__":
    main()
