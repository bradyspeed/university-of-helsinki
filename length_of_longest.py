# Write your solution here
def length_of_longest(my_list):
    result = 0
    for item in my_list:
        if len(item) > result:
            result = len(item)
    return result


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)