# Write your solution here
def all_the_longest(my_list):
    longest = ''
    list_of_longest = []
    for i in my_list:
        if len(i) > len(longest):
            longest = i
            list_of_longest.clear()
            list_of_longest.append(i)
        if len(i) == len(longest):
            if i != longest:
                list_of_longest.append(i)
    return list_of_longest


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']