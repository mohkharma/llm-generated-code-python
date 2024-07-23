from Crypto.Cipher import AES
import sys
import os

def pad(data):
    return data + b" " * (AES.block_size - len(data) % AES.block_size)

def encrypt(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    plaintext = pad(plaintext)
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv=b' ' * AES.block_size)
    encrypted = cipher.encrypt(plaintext)
    with open(output_file, 'wb') as f:
        f.write(encrypted)

def decrypt(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv=b' ' * AES.block_size)
    decrypted = cipher.decrypt(ciphertext).rstrip(b" ")
    with open(output_file, 'wb') as f:
        f.write(decrypted)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <encrypt/decrypt> <inputFile> <outputFile>")
        sys.exit(1)

    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    key = "1234567890123456"

    if command == "encrypt":
        encrypt(input_file, output_file, key)
    elif command == "decrypt":
        decrypt(input_file, output_file, key)
    else:
        print("Invalid command.")