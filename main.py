from menu import Menu

if __name__ == "__main__":
    while True:
        Menu.print_menu()
        choice = input("Enter your choice: ")
        if not Menu.handle_choice(choice):
            print("Exiting the program.")
            break


