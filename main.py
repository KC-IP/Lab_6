# Aidan Boudreau & Wen Qian Chen
# Encode or decode password by adding or subtracting 3
def password_encoder(password):
   encoded_password = ''
   for digit in password:
       # Add 3 to each digit
       encoded_digit = str((int(digit) + 3) % 10)
       encoded_password += encoded_digit
   return encoded_password


def password_decoder(encode_password):
   password = ''
   for digit in encode_password:
       # Subtract 3 to each digit
       decoded_digit = str((int(digit) - 3) % 10)
       password += decoded_digit
   return password


def main():
   # menu options
   while True:
       print("Menu")
       print("-------------")
       print("1. Encode")
       print("2. Decode")
       print("3. Quit\n")


       option = input("Please enter an option: ")


       if option == "1":
           password = input("Please enter your password to encode: ")
           encoded_password = password_encoder(password)
           print("Your password has been encoded and stored!\n")


       elif option == "2":
           original_password = password_decoder(encoded_password)
           print("The encoded password is " + encoded_password + ", and the original password is " + original_password + ".\n")


       elif option == "3":
           break


       else:
           print("Invalid option. Please try again.\n")




if __name__ == '__main__':
   main()

