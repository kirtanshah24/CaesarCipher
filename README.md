# CaesarCipher
Python program to implement a Caesar cipher-based encryption and decryption system with additional functionality for brute-force attacks
  The goal of this program is to implement a Caesar cipher-based encryption and decryption system with additional functionality for brute-force attacks. The program allows users to:
  
1. Encrypt a given plaintext word using a randomly generated shift key.
2. Decrypt the ciphertext using the same key.
3. Store the encrypted and decrypted text in separate files (encrypt.txt and decrypt.txt).
4. Validate plaintext input to ensure it consists only of lowercase English letters and is a valid English word.
5. Perform a brute-force attack by trying all possible 26 shift values, logging all attempts, and identifying valid English words from the decrypted outputs.
6. Provide a user-friendly interface for input and decision-making.

  This system helps users understand the vulnerabilities of the Caesar cipher by demonstrating how easily encrypted messages can be decrypted through brute-force attacks. It also ensures file-based data persistence for later analysis.
