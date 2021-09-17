import random

from django.contrib.admin.templatetags.admin_list import results

from similar_characters import cool_alphabet, BIGTEXT


def alteration_func(char):
    """
    This function replaces `char` with a randomly picked character from values that match
    it in `cool_alphabet`
    :param char: A character we want to modify
    :return: The modified/changed character
    """
    for key in cool_alphabet:
        if key == char:
            if len(cool_alphabet[key]) >= 2:
                my_list = cool_alphabet[key]
                in_key = random.randrange(len(my_list) - 1)
                print(my_list[in_key])
                return my_list[in_key]
            else:
                print(cool_alphabet[key])
                return cool_alphabet[key]
            return cool_alphabet[key]



def replace_char(password, char, step):
    """
    replace the character in password at the step
    :param password: the `result` string
    :param char: the `char` we wish to replace
    :param step: the location of that character we want to replace
    :return:
    """
    return password.replace(password[step], char)


def should_we_alter(password):
    """
    decide if we should alter or not, based on a random step in the string
    if the character at the alteration step isn't in cool_alphabet
    then we just repeat again
    :param password:
    :return:
    """
    alteration_step = random.randrange(len(password) - 1)
    results_alt = password[alteration_step]
    print(results_alt)
    if results_alt in cool_alphabet:
        print("Yay, we have found a change for your result")
        character_to_change = alteration_func(results_alt)
        strings = replace_char(password, character_to_change, alteration_step)
        return strings
    else:
        return password

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
included_word = BIGTEXT  # str(input("Please enter a word or number you would like to include in your password: "))
passlen = int(input("Please enter a password length to randomly generate: "))
if passlen >= len(included_word):
    p = "".join(random.sample(s, passlen))
    length_included_word = "".join(p[:len(included_word)])
    result = p.replace(length_included_word, included_word)
    print("result:", result)
else:
    print("Please start again")

inputs = ""
while inputs != "0":

    inputs = input("Would you like to add some changes? press enter; 0 to exit")
    if inputs == "":
        final_list = should_we_alter(result)
        print("Final result:", final_list)
        result = final_list

# def prac_generate_password():
#     s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#     included_word = str(input("Please enter a word or number you would like to include in your password: "))
#     passlen = int(input("Please enter a password length to randomly generate: "))
#     if passlen > len(included_word):
#         p = "".join(random.sample(s, passlen))
#         length_included_word = "".join(p[:len(included_word)])
#         result = p.replace(length_included_word, included_word)
#     else:
#         print("Please start again")
#
#     print(result)
