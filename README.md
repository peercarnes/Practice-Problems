# Practice Problems
 Just some practice problems I messed around with in my free time. Be aware, there are bugs

These two are the main functions that took some time. The others are just smaller, easier practice problems

AS OF 9/15/2021 11pm MST, the code f or password generator isn't completely finsihed, and technically neither the caesar code.


Caesar.py
def caesar_cipher(strings, shift):
    """
    This function looks at every character in `strings`
    :param strings: str: the initial string you want to enter
    :param shift: int: the amount of places forward in the alphabet
        the user would like to `shift` each character too.
    :return: str: returns the same string except every character in the string
        is `shifted` forward
    """



Password_generator.py
def alteration_func(char):
    """
    This function replaces `char` with a randomly picked character from values that match
    it in `cool_alphabet`
    :param char: A character we want to modify
    :return: The modified/changed character
    """
def replace_char(password, char, step):
    """
    replace the character in password at the step
    :param password: the `result` string
    :param char: the `char` we wish to replace
    :param step: the location of that character we want to replace
    :return:
    """
def should_we_alter(password):
    """
    decide if we should alter or not, based on a random step in the string
    if the character at the alteration step isn't in cool_alphabet
    then we just repeat again
    :param password:
    :return:
    """




