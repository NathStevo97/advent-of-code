# Part 1
with open('./inputs/input_1.txt') as file:
    columns = list(zip(*(map(int, row.split()) for row in file))) # # Open file and split rows into columns

# Sort each column into numerically ascending order
sortedColumn1 = sorted(columns[0], key=int, reverse=False)
sortedColumn2 = sorted(columns[1], key=int, reverse=False)

diffs = []

# calculate the absolute difference between each row's values
for i in range(0, len(columns[0])):
    rowDiff = abs(sortedColumn2[i] - sortedColumn1[i])
    diffs.append(rowDiff)

totalDiffs = sum(diffs)
print(f"Sum of differences across each row: {totalDiffs}")

# Part 2

similarityScore = 0

for i in sortedColumn1:
    column2Count = sortedColumn2.count(i)
    similarityScore = similarityScore + i * column2Count

print(f"Final Similarity Score {similarityScore}")