import random

characters = " " +"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/*!~@#$%^&()|\/<>:;"
characters = list(characters)
key = characters.copy()
random.shuffle(key)
# print(key)


def Encrypt():
    plain_text = input("\nEnter The Message To Encrypt : ")
    cipher_text = " "

    for letter in plain_text:
        index = characters.index(letter)
        cipher_text += key[index]

    print("\nOriginal Message is :",plain_text)
    print(f"\nEncrypted Message is : {cipher_text} \n\n===========================================================")

    return


def Decrypt():
    cipher_text = input("Enter The Message To Decrypt : ")
    plain_text = " "


    for letter in cipher_text:
        index = key.index(letter)
        plain_text += characters[index]

    print(f"Original Message is : {plain_text} \n\n===========================================================")
    return


def Substitution_Cipher():
    while True:
        user_input = input('''\n\nWhat do you want to perform?
        1.Encryption
        2.Decryption
        3.Exit : \n--> ''')

        if user_input == "1":
            print("\n****** YOU HAVE SELECTED ENCRYPTION PROCESS *****")
            Encrypt()
        elif user_input == "2":
            print("\n****** YOU HAVE SELECTED DECRYPTION PROCESS *****")
            Decrypt()
        else:
            print("Exiting...........")
            break
            
            
Substitution_Cipher()


