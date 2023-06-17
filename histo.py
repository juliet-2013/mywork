import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 7, 7, 7]

# Create a histogram
plt.hist(data, bins=range(min(data), max(data) + 2), edgecolor='black')

# Set labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')

# Display the histogram
plt.show()
