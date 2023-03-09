# Define the main function
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            encode_password()
        elif option == "2":
            decode_password()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
