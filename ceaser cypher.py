# Caesar Cipher Tool with Brute Force Option

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def brute_force(cipher_text):
    print("\nTrying all possible shifts:\n")
    for shift in range(1, 26):
        print("Shift", shift, ":", decrypt(cipher_text, shift))


def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force (Try all shifts)")

    choice = input("Choose option: ")

    if choice == "1":
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        print("Encrypted Message:", encrypt(message, shift))

    elif choice == "2":
        message = input("Enter encrypted message: ")
        shift = int(input("Enter shift value: "))
        print("Decrypted Message:", decrypt(message, shift))

    elif choice == "3":
        cipher = input("Enter encrypted message: ")
        brute_force(cipher)

    else:
        print("Invalid option")


main()