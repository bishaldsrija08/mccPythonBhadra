import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 2, 3, 8, 16]


plt.plot(x, y1, label = "Line 1", color = "blue")
plt.plot(x, y2, label = "Line 2", color = "green")
plt.title("Sample line graph")
plt.xlabel("X-axis label")
plt.ylabel("Y-axis label")
plt.legend()
plt.grid(True)
plt.show()