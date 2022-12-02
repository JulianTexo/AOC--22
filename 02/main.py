import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    contents = [line.rstrip() for line in f]

#Part one!
score = 0
for line in contents:
    oponent_pick, my_pick = line.split(" ")
    if my_pick == 'X':
        score += 1
        if oponent_pick == 'A':
            score += 3
        elif oponent_pick == 'C':
            score += 6
    elif my_pick == 'Y':
        score += 2
        if oponent_pick == 'A':
            score += 6
        elif oponent_pick == 'B':
            score += 3
    elif my_pick == 'Z':
        score += 3
        if oponent_pick == 'B':
            score += 6
        elif oponent_pick == 'C':
            score += 3

#Solution Part one!
print("Result is: " + str(score))

#Part two!
score = 0
for line in contents:
    oponent_pick, result_needed = line.split(" ")
    #Oponent picks rock
    if oponent_pick == 'A':
        #need to loose (0 points) so pick scissors (3 points)
        if result_needed == 'X':
            score += 3
        #need to draw (3 points) so pick rock (1 point)
        elif result_needed == 'Y':
            score += 4
        #need to win (6 points) so pick paper (2 points)
        elif result_needed == 'Z':
            score += 8
    #oponent picks paper
    elif oponent_pick == 'B':
        #need to loose (0 points) so pick rock (1 point)
        if result_needed == 'X':
            score += 1
        #need to draw (3 points) so pick paper (2 points)
        elif result_needed == 'Y':
            score += 5
        #need to win (6 points) so pick scissors (3 points)
        elif result_needed == 'Z':
            score += 9
    #oponent picks scissors
    elif oponent_pick == 'C':
        #need to loose (0 points) so pick paper (2 points)
        if result_needed == 'X':
            score += 2
        #need to draw (3 points) so pick scissors (3 points)
        elif result_needed == 'Y':
            score += 6
        #need to win (6 points) so pick rock (1 point)
        elif result_needed == 'Z':
            score += 7
print("result part two: " + str(score))