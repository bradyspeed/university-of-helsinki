# Write your solution here
def longest(strings: list):
    longest_word = ''
    for n in strings:
        if len(n) > len(longest_word):
            longest_word = n
    return longest_word





if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))