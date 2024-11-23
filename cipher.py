alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text ,shift_amount):
    cipher_text=""
    for letter in original_text:

        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"your encoded word:{cipher_text}")


def decrypt(original_text, shift_amount):
    og_code = ""
    for letter in original_text:
        if letter not in alphabet:
            og_code += letter
        else:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            og_code += alphabet[shifted_position]
    print(f"your decoded word:{og_code}")


def cipher(original_text, shift_amount, encode_or_decode):
    if encode_or_decode == "encode":
        encrypt(text,shift)


    elif encode_or_decode == "decode":
        decrypt(text,shift)

cipher(text,shift,direction)





