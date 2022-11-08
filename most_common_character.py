# Write your solution here
def most_common_character(str):
    most = str[0]
    for i in str:
        if str.count(i) > str.count(most):
            most = i
    return most



if __name__ == "__main__":
    first_string = "aaaabcde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))

