import random
import string
import os
import enchant

# Encryption Function
def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char in string.ascii_lowercase:
            shifted = (ord(char) - ord('a') + key) % 26 + ord('a')
            ciphertext += chr(shifted)
    return ciphertext

# Decryption Function
def decrypt(ciphertext, key):
    decrypted_text = ''
    for char in ciphertext:
        if char in string.ascii_lowercase:
            shifted = (ord(char) - ord('a') - key) % 26 + ord('a')
            decrypted_text += chr(shifted)
    return decrypted_text

# File functions
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Creating files if not present
def check_and_create_files():
    if not os.path.exists('plaintext.txt'):
        with open('plaintext.txt', 'w') as file:
            file.write("default")
        print("File 'plaintext.txt' created. Please edit it with some text.")

    if not os.path.exists('encrypt.txt'):
        open('encrypt.txt', 'w').close()
        print("File 'encrypt.txt' created.")

    if not os.path.exists('decrypt.txt'):
        open('decrypt.txt', 'w').close()
        print("File 'decrypt.txt' created.")

    if not os.path.exists('log.txt'):
        open('log.txt', 'w').close()
        print("File 'log.txt' created.")
    
    if not os.path.exists('multiple_match.txt'):
        open('multiple_match.txt', 'w').close()
        print("File 'multiple_match.txt' created.")

# Validate plaintext
def validate_plaintext(plaintext):
    if not all(char in string.ascii_lowercase for char in plaintext):
        raise ValueError("Plaintext should only contain lowercase alphabets and no spaces.")
    
    english_dict = enchant.Dict("en_US")
    if not english_dict.check(plaintext):
        raise ValueError("Plaintext is not a valid English word.")

# Brute-force attack function
def brute_force_attack():
    ciphertext = read_file('encrypt.txt')
    english_dict = enchant.Dict("en_US")
    with open('log.txt', 'w') as log_file:
        matches = []
        for key in range(26):
            decrypted_text = decrypt(ciphertext, key)
            
            log_file.write(f"Key: {key}, Decrypted text: {decrypted_text}\n")
            
            # Using enchant, if word in dictionary, store in multiple_match.txt
            if english_dict.check(decrypted_text):
                match_entry = f"Key: {key}, Decrypted Text: {decrypted_text}"
                matches.append(match_entry)
        
        # Write matching entries to multiple_match.txt
        with open('multiple_match.txt', 'w') as multiple_file:
            for match in matches:
                multiple_file.write(match + "\n")

# Enter word to encrypt
def get_plaintext_input():
    user_input = input("Enter a word to perform Caesar cipher on (only lowercase letters, no spaces): ").strip()
    
    if not user_input.isalpha() or not user_input.islower():
        raise ValueError("Invalid input. Please enter only lowercase alphabets with no spaces.")
    
    # Write the word to plaintext file
    write_file('plaintext.txt', user_input)
    print(f"Your input '{user_input}' has been saved to 'plaintext.txt'.")

# User choice for continuing or exiting
def user_choice():
    while True:
        choice = input("Enter '1' to Continue and '2' to Exit: ").strip()
        if choice == '1':
            return True  
        elif choice == '2':
            print("Exiting the program.")
            return False  
        else:
            print("Invalid choice. Please enter again.")

# Main function
def main():
    # Check for files
    check_and_create_files()

    while True:  # Infinite loop until the user chooses to exit

        # Enter word
        custom_word_choice = input("Do you want to enter a custom word for encryption? (y/n): ").strip().lower()
        if custom_word_choice == 'y':
            try:
                get_plaintext_input()
            except ValueError as e:
                print(e)
                continue  # Return to the start of the loop to try again

        plaintext = read_file('plaintext.txt')
        try:
            validate_plaintext(plaintext)
        except ValueError as e:
            print(e)
            continue  # Return to the start of the loop to try again

        # Key Generation
        key = random.randint(0, 25)
        print(f"Generated Key: {key}")
        
        # Encrypt the text
        ciphertext = encrypt(plaintext, key)
        write_file('encrypt.txt', ciphertext)
        
        # Decrypt the ciphered text
        decrypted_text = decrypt(ciphertext, key)
        write_file('decrypt.txt', decrypted_text)
        
        # Verify manually if text is correctly encrypted and decrypted
        print("Encryption and decryption done.\nCheck decrypt.txt to verify if it matches the original plaintext.")
        
        # Brute Force Attack and log it
        brute_force_attack()
        print("Brute force attack complete. \nCheck log.txt for details and multiple_match.txt for valid English words.")
        
        # Ask the user if they want to continue or exit
        if not user_choice():
            break  

if __name__ == "__main__":
    main()
