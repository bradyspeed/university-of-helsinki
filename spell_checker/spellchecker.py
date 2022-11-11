# write your solution here
text = input('Write text: ')

words = []
with open("wordlist.txt") as new_file:
    for line in new_file:
       for line in new_file:
            line = line.replace('\n', '')
            words.append(line)

res = text.split()
for word in res:
    if word.casefold() in words:
        print(word, end=' ')
    elif word.casefold() == 'a':
        print(word, end=' ')
    else:
        print(f'*{word}*', end=' ')