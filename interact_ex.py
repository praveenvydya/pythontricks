from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display
from io import BytesIO
import numpy as np
from matplotlib import pyplot as plt
from flask import Flask, send_file

def main():
    #return image_()
    w = widgets.IntSlider
    return w


if __name__ == "__main__":
    main()

def image_():
    x = np.random.uniform(0, 5, size=100)
    ep = np.random.normal(size=100)
    y = 2 * x + ep
    plt.scatter(x, y)
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')