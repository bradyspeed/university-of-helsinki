# Write your solution here
def everything_reversed(my_list: list):
    new_list = []
    for my_string in my_list:
        new_list.append(my_string[::-1])
    return new_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)