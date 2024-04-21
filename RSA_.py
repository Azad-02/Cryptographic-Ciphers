import random
import math

def multiplicative_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return (gcd, y, x - (a // b) * y)
    
    gcd, x, y = extended_gcd(e, phi)
    if gcd != 1:
        return None
    else:
        return x % phi

def gen_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Selecting a random e coprime with phi
    while True:
        e = random.randrange(2, phi) 
        if math.gcd(e, phi) == 1:
            break
    
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = [chr((int(char) ** d) % n) if (int(char) ** d) % n < 128 else '#' for char in ciphertext]
    return ''.join(plain)


public_key, private_key = gen_keypair(7, 11)

def RSA_Cipher():
    while True:
        user_input = input('''\n\nWhat do you want to perform?
        1.Encryption
        2.Decryption
        3.Exit : \n--> ''')

        if user_input == "1":
            print("\n****** YOU HAVE SELECTED ENCRYPTION PROCESS *****")
            message = input("\nEnter The Message To Encrypt : ")
            cipher = encrypt(public_key, message)
            print("\nOriginal Message is :",message)
            print(f"\nEncrypted Message is : {cipher} \n\n===========================================================")
        elif user_input == "2":
            print("\n****** YOU HAVE SELECTED DECRYPTION PROCESS *****")
            cipher_text = input("Enter The Message To Decrypt : ")
            cipher = [int(c) for c in cipher_text.split(',')] 
            plain = decrypt(private_key, cipher)
            print(f"Original Message is : {plain} \n\n===========================================================")

            
        else:
            print("Exiting...........")
            break
            
RSA_Cipher()

