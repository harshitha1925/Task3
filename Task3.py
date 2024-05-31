#TASK 3
#PASSWORD GENERATOR
import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper= string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    all_characters = lower + upper + digits + punctuation

    password = ' '.join(random.choice(all_characters)  for _ in range (length))

    if (any(c in lower for c in password) and
        any(c in upper for c in password) and
        any(c in digits for c in password) and
        any(c in punctuation for c in password)) :
        return password

def get_password_length():
    while True :
        try:                                
            length = int(input("Enter the desired length for the password (minimum 8 characters):"))
            if length < 8:
                print ("Password length should be at least 8 characters.")
            else :
                return length
        except ValueError:
            print ("Invalid input. Please Enter a numeric value.")

def main():
    print ("Password Generator")
    length = get_password_length()
    password = generate_password(length)
    print (f"Generated Password: {password}")

if __name__== "__main__" :
    main()
