import random


def encryption(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""

    for i in range(0, len(message)):
        character = message[i]
        ciphertext = ciphertext + character

        for j in range(0, key):
            ciphertext = ciphertext + random.choice(alphabet)

    return ciphertext


message: str = input("Enter a message to encrypt:")
key = int(input("Put any number between 1 and 10:"))

while not (key >= 1 and key <= 10):
    print("Invalid key, try again!")
    key = int(input("Put any number between 1 and 10:"))

ciphertext: str = encryption(message, key)
print("Your Ciphertext is:")
print(ciphertext)
