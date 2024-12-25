import matplotlib.pyplot as plt
import random
import time

def bubble_sort_visualization(data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                visualize(data)
                time.sleep(0.1)  # Pause to see the changes

def visualize(data):
    plt.bar(range(len(data)), data, color="yellow")
    plt.pause(0.05)
    plt.clf()

# Generate random data
data = [random.randint(10, 100) for _ in range(20)]

plt.ion()
visualize(data)
bubble_sort_visualization(data)
plt.ioff()
plt.show()
