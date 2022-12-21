# A and X = Rock
# B and Y = Paper
# C and Z = Scissors

# Points:
## 1 for X, 2 for Y, 3 for Z
## 0 for loss, 3 for draw, 6 for win

with open('./input.txt') as file:
    rounds = file.read().split('\n') # read input file and split into groups based on 2 blank lines

#print(rounds)

outcomesPart1 = {
    'A X': 3+1,
    'A Y': 6+2,
    'A Z': 0+3,
    'B X': 0+1,
    'B Y': 3+2,
    'B Z': 6+3,
    'C X': 6+1,
    'C Y': 0+2,
    'C Z': 3+3,
}

#print(outcomesPart1)

resultPart1 = sum([outcomesPart1[round] for round in rounds])
print("Total Score (Part 1): ", resultPart1)

# Part 2:
## X = Need to lose => 0 points
## Y = Need to draw => 3 points
## Z = Win => 6 points

outcomesPart2 = {
    'A X': 0+3, # A = rock, to lose means picking scissors = 3 points
    'A Y': 3+1, # A = rock, to draw means picking rock = 1 points
    'A Z': 6+2, # A = rock, to win means picking paper = 2 points
    'B X': 0+1, # B = paper, to lose means picking rock = 1 points
    'B Y': 3+2, # B = paper, to draw means picking paper = 2 points
    'B Z': 6+3, # B = paper, to win means picking scissors = 3 points
    'C X': 0+2, # C = scissors, to lose means picking paper = 2 points
    'C Y': 3+3,  # C = scissors, to draw means picking scissors = 3 points
    'C Z': 6+1, # C = scissors, to win means picking rock = 1 points
}

resultPart2 = sum([outcomesPart2[round] for round in rounds])
print("Total Score (Part 2): ", resultPart2)