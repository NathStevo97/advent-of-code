# Each elf's inventory is separated by a blank line
# Loop through lines and add up all entries separated by blank lines
# Find position of elf with most calories and the value (max) and get position of max

with open('./input.txt') as file:
    groups = file.read().split('\n\n') # read input file and split into groups based on 2 blank lines

groups = [group.split('\n') for group in groups]

totals = [sum([int(x) for x in group]) for group in groups]

part_1 = max(totals) # get maximum
print("Part 1 Answer (Largest amount carried): ", part_1)
totals.sort(reverse=True) # sort list in decending order
part_2 = sum(totals[:3]) # add first 3 of sorted list together (indices 0-2)
print("Part 2 Answer (Total amount carried of top 3): ",part_2)