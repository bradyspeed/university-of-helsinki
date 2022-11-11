# write your solution here
def largest():
    lst = []
    with open('numbers.txt') as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            lst.append(line)
            lst = [int(i) for i in lst]
        return max(lst)



if __name__ == "__main__":
    print(largest())