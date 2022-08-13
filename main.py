import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caeser(start_text, movement, choice):
    cypher_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if choice == "encode":
                new_position = position + movement
            elif choice == "decode":
                new_position = position - movement
            cypher_text += alphabet[new_position]
        else:
            cypher_text += char
    print(f"The {choice}d text is: {cypher_text}")


cont = True
while cont:
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("Please type 'encode' or 'decode'.\n")
        continue
    text = input("Type your message:\n").lower()
    if text.isalpha() == False:
        print("Please type only letters.\n")
        continue
    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Please type only numbers.\n")
        continue
    else:
        shift = shift % 26

    caeser(start_text=text, movement=shift, choice=direction)

    more = input("\nType 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if more == "no":
        cont = False
        print("Goodbye.")







# OLD CODE BEFORE CONSOLIDATION
# def encode(text, shift):
#     cypher_text = ""
#     for char in text:
#         position = alphabet.index(char)
#         new_position = position + shift
#         cypher_text += alphabet[new_position]
#     print(f"The encoded text is {cypher_text}.")
#
#
# def decode(text, shift):
#     cypher_text = ""
#     for char in text:
#         position = alphabet.index(char)
#         new_position = position - shift
#         cypher_text += alphabet[new_position]
#     print(f"The decoded text is {cypher_text}.")
#
#
# if direction == "encode":
#     encode(text, shift)
# elif direction == "decode":
#     decode(text, shift)