alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceaser(start_text,shift_amount,ceaser_direction):
    end_text = " "
    if ceaser_direction == "encode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_poistion = position + shift_amount
            end_text += alphabet[new_poistion]
        else:
            end_text += char
    print(f"Here's the {ceaser_direction}d result: {end_text}")

from art import logo
print(logo)


should_end = False
while not should_end:
     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
     text = input("Type your message:\n").lower()
     shift = int(input("Type the shift number:\n"))

     shift = shift % 26


     ceaser(start_text=text, shift_amount=shift, ceaser_direction=direction)

     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
     if restart == "no":
        should_end = True
        print("Goodbye")



    