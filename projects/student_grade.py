import matplotlib.pyplot as plt

# Student grades dictionary
grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 90,
    'Eva': 88,
    'Frank': 75,
    'Grace': 95
}

# names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace"]
# scores = [85, 92, 78, 90, 88, 75, 95]

# Extract names and scores
names = list(grades.keys())
scores = list(grades.values())

# Create a pie chart
plt.pie(scores, labels=names, autopct='%1.1f%%', startangle=140)
plt.title('Student Grade Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Plotting the bar chart

plt.bar(names, scores, color='skyblue')
plt.title('Student Grades')
plt.xlabel('Students')
plt.ylabel('Grades')
plt.ylim(0, 100)

plt.show()