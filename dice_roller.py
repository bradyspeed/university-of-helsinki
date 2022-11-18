# Model solution for reference
from random import sample

""" def roll(die: str):
    dices = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
 
    return sample(dices[die], 1)[0]

def play(die1: str, die2: str, times: int):
    v1 = 0
    v2 = 0
    t = 0
    for i in range(times):
        n1 = roll(die1)
        n2 = roll(die2)
        if n1>n2:
            v1 += 1
        elif n1<n2:
            v2 += 1
        else:
            t += 1
    return v1, v2, t """

# Write your solution here
from random import choice

# This function rolls the die specified by the argument
def roll(die: str):
    
    # Non-transitive dice tables
    die_a = [3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]
    
    if die == 'A':
        return choice(die_a)
    if die == 'B':
        return choice(die_b)
    if die == 'C':
        return choice(die_c)

# This function throws 2 dice a specified number of times and returns a tuple with record of win / loss / tie
def play(die1: str, die2: str, times: int):
    rolls_1 = []
    rolls_2 = []
    score = [0, 0, 0]
    for n in range(times):
        if die1 == 'A':
            rolls_1.append(roll('A'))
        if die1 == 'B':
            rolls_1.append(roll('B'))
        if die1 == 'C':
            rolls_1.append(roll('C'))
        if die2 == 'A':
            rolls_2.append(roll('A'))
        if die2 == 'B':
            rolls_2.append(roll('B'))
        if die2 == 'C':
            rolls_2.append(roll('C'))
    for i in range(times):
        if rolls_1[i] > rolls_2[i]:
            score[0] += 1
        if rolls_1[i] < rolls_2[i]:
            score[1] += 1
        if rolls_1[i] == rolls_2[i]:
            score[2] += 1
    return tuple(score)



if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")

    result = play("A", "C", 100)
    print(result)
    result = play("B", "B", 100)
    print(result)