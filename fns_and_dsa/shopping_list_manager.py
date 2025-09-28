def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the item to add: ")
            shopping_list.append(name)
        elif choice == '2':
            name = input("Enter the item to remove: ")
            if name in shopping_list:
                shopping_list.remove(name)
            else:
                print ("There is no item with this name.")
        elif choice == '3':
            for item in shopping_list:
                print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
