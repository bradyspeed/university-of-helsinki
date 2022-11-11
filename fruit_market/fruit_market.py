# write your solution here
def read_fruits():
    fruit_dict = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            temp_num = float(parts[1])
            #print(parts)
            fruit_dict[parts[0]] = temp_num
    return fruit_dict


if __name__ == "__main__":
    print(read_fruits())