# Write your solution here
from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    ascii = ''
    punc = ''
    other = ''
    for i in my_string:
        if i in ascii_letters:
            ascii += i
        elif i in punctuation:
            punc += i
        else:
            other += i
    my_tuple = (ascii, punc, other)
    return my_tuple



if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])