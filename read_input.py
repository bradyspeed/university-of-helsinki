# Write your solution here
def read_input(user_prompt, floor, ceiling):
    while True:
        try:
            input_str = input('Please type in a number: ')
            num = int(input_str)
            if num > floor and num < ceiling:
                return num
        except ValueError:
            pass
    
        print(f'You must type in an integer between {floor} and {ceiling}')




if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)