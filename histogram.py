# Write your solution here
def histogram(string):
    characters = {}
    for i in range(0, len(string)):
        if string[i] not in characters:
            characters[string[i]] = 0
        characters[string[i]] += 1
    for character, qty in characters.items():
        stars = "*"*qty
        print(f"{character} {stars}")



if __name__ == "__main__":
    histogram("statistically speaking")