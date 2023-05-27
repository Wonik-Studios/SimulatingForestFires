from datetime import datetime
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import os

def generate_noise(xpix, ypix):
    noise = PerlinNoise(octaves=10)
    pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    now = datetime.now()

    plt.imshow(pic, cmap='gray')
    plt.savefig("LandscapeGraphs" + os.sep + now.strftime('%m-%d-%Y_%H-%M-%S') + ".png")
    return pic

if __name__ == "__main__":
    generate_noise(800, 600)
