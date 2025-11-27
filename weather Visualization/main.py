import matplotlib.pyplot as plt

# Read data from file
dates  = []
temperatures = []

try:
    with open('weather.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts)==2:
                date, temp = parts
                dates.append(date)
                temperatures.append(int(temp))
except FileNotFoundError:
    print("The file 'weather.txt' was not found.")
    exit()
    

# Plot the data
plt.figure(figsize=(10, 5)) #Make a big drawing paper of size 10 by 5.
plt.plot(dates, temperatures, marker='o', linestyle='-', color='skyblue')
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.tight_layout() #Arrange everything neatly so nothing overlaps.
plt.show()