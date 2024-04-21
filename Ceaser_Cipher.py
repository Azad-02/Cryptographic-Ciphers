Alphabets = "abcdefghijklmnopqrstuvwxyz"
numberofletters = len(Alphabets)
print("*******CEASER CIPHER*******")
def Encryption(Plain_Text ,Key):
        cipher_text = ''
        for letter in Plain_Text :
            letter  = letter.lower()
            if not letter == ' ':
                Index = Alphabets.find(letter)
                if Index == -1:
                    cipher_text += letter
                else:
                    new_index =Index + key
                    if new_index >= numberofletters:
                        new_index -= numberofletters
                    cipher_text += Alphabets[new_index]
        return cipher_text


def Decryption(cipher_text ,Key):
        Plain_Text = ''
        for letter in cipher_text :
            letter  = letter.lower()
            if not letter == ' ':
                Index = Alphabets.find(letter)
                if Index == -1:
                    Plain_Text += letter
                else:
                    new_index =Index + key
                    if new_index < 0: 
                        new_index += numberofletters
                    Plain_Text += Alphabets[new_index]
        return Plain_Text


while True:
    user_input = input('''What Do You Want To Do ?
    1.Perform Encryption
    2.Perform Decryption
    3.Press 0 To Exit ''').upper()

    if user_input == "1":
        print("\n----You've Selected The Option To Encrypt The Plain Text Into Cipher Text----\n")
        key = int(input("Enter The Key Between 1 To 26: "))
        text = input("Enter The Plain Text That You Want To Encrypt: ")
        cipher_text = Encryption(text,key)
        print(f'Your Encrypted Cipher Text  is: {cipher_text}')

    elif user_input == "2":
        print("\n----You've Selected The Option To Decrypt The Cipher Text Into Original Plain Text----\n")
        key = int(input("Enter The Key Between 1 To 26: "))
        text = input("Enter The Plain Text That You Want To Decrypt: ")
        Plain_Text = Decryption(text,key)
        print(f'Your Decrypted Plain Text  is: {Plain_Text}')
    else:
        print("Exiting.....")
        break
        
