from datetime import datetime
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import sys

def generate_noise(xpix, ypix):
    noise = PerlinNoise(octaves=10, seed=1)
    pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    now = datetime.now()
    if (sys.platform == "Windows"):
        delimiter = "\"
    else:
        delimiter = "/"

    plt.imshow(pic, cmap='gray')
    plt.savefig(f"LandscapeGraphs{delimiter}{now.strftime('%m-%d-%Y_%H:%M:%S')}")
    return pic

if __name__ == "__main__":
    generate_noise(800, 600)
