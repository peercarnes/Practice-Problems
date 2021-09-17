letter = None


def caesar_cipher(strings: str, shift: int) -> str:
    for i in strings:
        char_position = alphabet.find(i)
        # print(char_position)
        if (char_position + shift) >= (len(alphabet) - 1):
            left_over = len(alphabet) - char_position
            # print(left_over)
            if left_over - shift <= 0:
                negative = shift - left_over
                # print(negative)
                i = alphabet[negative]
                contents.append(i)
        else:
            next_char = char_position + shift
            i = alphabet[next_char]
            contents.append(i)
    print("".join(contents))


while letter != "0":
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = input("Hello, Please add a string to cipher: ")
    s = int(input("Please enter the magical number that makes our text look funny: "))
    contents = []
    caesar_cipher(letter, s)
    letter = input("Please click enter to continue, or 0 to finish: ")
