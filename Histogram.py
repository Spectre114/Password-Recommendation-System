import matplotlib.pyplot as plt
import numpy as np
import csv

ce = 0  # Easy as rated by the user
cm = 0  # Moderate as rated by the user
ch = 0  # Hard as rated by the user

# Read data from Form-1-report.csv
with open("Form-1-report.csv") as file1:
    rd1 = csv.reader(file1, delimiter=',')
    for cont in rd1:
        for i in range(len(cont)):
            if cont[i] == "Easy":
                ce += 1
            elif cont[i] == "Moderate":
                cm += 1
            else:
                ch += 1

# Read data from Form-2-report.csv
with open("Form-2-report.csv") as file2:
    rd2 = csv.reader(file2, delimiter=',')
    for cont in rd2:
        for i in range(len(cont)):
            if cont[i] == "Easy":
                ce += 1
            elif cont[i] == "Moderate":
                cm += 1
            else:
                ch += 1

file1.close()
file2.close()

# Prepare the data for the histogram
# Adjusting factor is 25 as each password is rated by 25 users
counts_u = [ce / 25, cm / 25, ch / 25]
counts_m = [20, 20, 20]
diff = ['Easy\nuser: 1-5\nprogram: 5-10', 'Moderate\nuser: 15-20\nprogram: 20-25', 'Hard\nuser: 30-35\nprogram: 35-40']

# Set the width of each bar
bar_width = 0.35

# Create the positions of the bars on the x-axis
user = np.arange(len(diff))
mc = user + bar_width

# Create the histogram with side-by-side bars
plt.bar(user, counts_u, bar_width, edgecolor='black', color='white', label = 'user')
plt.bar(mc, counts_m, bar_width, edgecolor='black', color='white', linestyle='dotted', label = 'program')

# Add labels and title
plt.xlabel('Difficulty', fontsize = 13)
plt.ylabel('Frequency', fontsize = 13)
plt.title('Rating Histogram')

# Set the x-axis tick labels
plt.xticks(user + bar_width/2, diff)

# Add a legend
plt.legend()

# Display the histogram
plt.show()
