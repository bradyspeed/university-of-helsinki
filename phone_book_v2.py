# Write your solution here
phone_book = {}


while True:
    command = int(input('command (1 search, 2 add, 3 quit): '))
    if command == 2:
        name = input('name: ')
        number = input('number: ')
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]
        print('ok!')
        continue
    elif command == 1:
        name = input('name: ')
        if name not in phone_book:
            print('no number')
            continue
        print(*phone_book[name], sep='\n')
        continue
    print('quitting...')
    break