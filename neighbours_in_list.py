# Write your solution here
def longest_series_of_neighbours(lst):
    longest = 1
    result = 1
    for i in range(1, len(lst)):
        if abs(lst[i-1]-lst[i]) == 1:
            result += 1
        else:
            result = 1
        longest = max(longest, result)
    return longest



if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10]
    print(longest_series_of_neighbours(my_list))