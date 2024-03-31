alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text +=alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here is the Text after encryption : {cipher_text}")
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text +=alphabet[new_position]
        else:
            plain_text += char
    print(f"Here is the Text after decryption : {plain_text}")

its_gone_end=False
while not its_gone_end:
    what_to_do=input("Type 'encrypt' for Encryption OR Type 'decrypt' for Decryption:\n").lower()
    text=input("Enter Your Message :\n").lower()
    shiftkey=int(input("Enter shift Key: \n"))

    if what_to_do == 'encrypt':
        encryption(text,shiftkey)
    elif what_to_do == 'decrypt':
        decryption(text,shiftkey)
    play_again=input("Type 'yes' To continue Or Type 'no' To Exit: \n").lower()
    if play_again == 'no':
        its_gone_end=True
        print("Have a nice Day! Bye....")