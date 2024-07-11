import matplotlib.pyplot as plt
import numpy as np

# easy(u) = 585
# modeerate(u) = 606
# hard(u) = 309

# Prepare the data for the histogram
counts_u = [585/25, 606/25, 309/25]        #adjusting factor is 25
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
plt.xlabel('Difficulty', fontsize = 12)
plt.ylabel('Frequency', fontsize = 12)
plt.title('Rating Histogram')

# Set the x-axis tick labels
plt.xticks(user + bar_width/2, diff,fontsize = 8)

# Add a legend
plt.legend()

# Display the histogram
plt.show()
