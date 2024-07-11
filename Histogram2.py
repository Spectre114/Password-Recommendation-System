import matplotlib.pyplot as plt
import numpy as np

# easy(u) = 585
# modeerate(u) = 606
# hard(u) = 309

# Prepare the data for the histogram
counts_u = [585/25, 606/25, 309/25]        #adjusting factor is 25
counts_m = [20, 20, 20]
diff = ['Easy', 'Moderate', 'Hard']

# Create the histogram
plt.bar(diff, counts_u, edgecolor='black', color='white', width=0.5, label = 'user')
plt.bar(diff, counts_m, edgecolor='black', color='white', width=0.4, linestyle='dotted', label = 'machine')

# Add labels and title
plt.xlabel('Difficulty')
plt.ylabel('Frequency')
plt.title('Rating Histogram')
plt.legend()

# Display the histogram
plt.show()
