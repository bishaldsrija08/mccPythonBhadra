import matplotlib.pyplot as plt

# Data
weeks = ["Week 1", "Week 2", "Week 3", "Week 4"]
student_A_hours = [10, 12, 8, 14]
student_B_hours = [9, 11, 17, 13]

# Create bar chart
plt.bar(weeks, student_A_hours, width=0.35, label="Student A", align='center')
plt.bar(weeks, student_B_hours, width=0.35, label="Student B", align='edge')

# Customize chart
plt.title("Weekly Study Hours Comparison")
plt.xlabel("Week")
plt.ylabel("Hours Studied")
plt.legend()

# Display chart
plt.show()