history_file = "history.txt"

while True:
    print("\n1. Add Command")
    print("2. View History")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        command = input("Enter command: ")
        with open(history_file, "a") as file:
            file.write(command + "\n")
        print("Command saved.")

    elif choice == "2":
        try:
            with open(history_file, "r") as file:
                print("\nCommand History:\n")
                print(file.read())
        except FileNotFoundError:
            print("No history found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
