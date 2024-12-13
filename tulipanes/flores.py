import matplotlib.pyplot as plt
import numpy as np

def draw_tulip():
    t = np.linspace(0, 2 * np.pi, 100)
    x = np.sin(t)
    y = np.cos(t) - 0.5
    plt.fill(x, y, color="green")

def draw_rose():
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 1 + np.sin(4 * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.fill(x, y, color="green")

def draw_cloud():
    t = np.linspace(0, 2 * np.pi, 100)
    x = 0.5 * np.cos(t)
    y = 0.5 * np.sin(t) + 0.5
    plt.fill(x, y, color="green")

plt.figure(figsize=(6, 8))

# Tulips
for i in range(3):
    plt.subplot(3, 1, i + 1)
    draw_tulip()
    draw_rose()
    draw_cloud()
    plt.axis("off")

plt.show()
