# Aidan Boudreau & Wen Qian Chen
# Define the main function
def encode(password):
    return password + "555"

def decode(encode_password):
    original_password = encode_password[:-3]
    return original_password
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encode_password = encode(password)
            print("Your password has been encoded and stored!")

        elif option == "2":
            encide_password = input("Please enter the encoded password: ")
            original_password = decode(encode_password)
            print("The encoded password is " + encoded_password + ", and the original_password is " + original_password + ".")

        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
if __name__ == '__main__':
    main()
