numbers = [1, 20, 30, 40, 55, 100, 11, 2, 2,4,6,77,88,23,4,5]

total = len(numbers) # Count the items in the list:
max = max(numbers) # Find the maximum value in the list:
min = min(numbers) # Find the minimum value in the list:
totalSum = sum(numbers) # Find the sum of all values in the list:

print(f"Total numbers: {total}")
print(f"Maximum number: {max}")
print(f"Minimum number: {min}")
print(f"Sum of all numbers: {totalSum}")


scores = [45,34]
print(scores)
if(scores==[]):
    print("The list is empty")
else:
    maxScore = max(scores)
    minScore = min(scores)
    totalScores = sum(scores)
    totalLength = len(scores)
    print(f"Highest score: {maxScore}")
    print(f"Lowest score: {minScore}")
    print(f"Total score: {totalScores}")
    print(f"Average score: {totalScores/totalLength}")

stock = ["banana", "orange", "mango", "apple"]
print(f"stock: {len(stock)}")

# intger funciton
sum()
min()
max()
len()