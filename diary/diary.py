# Write your solution here
while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    user_input = int(input('Function: '))
    if user_input == 0:
        print('Bye now!')
        break
    elif user_input == 1:
        new_entry = input('Diary entry: ')
        with open("diary.txt", "a") as my_file:
            my_file.write(f'{new_entry}\n')
    elif user_input == 2:
        with open("diary.txt") as new_file:
            contents = new_file.read()
            print(contents)