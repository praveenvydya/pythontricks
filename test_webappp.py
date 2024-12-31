from IPython.display import display
from io import BytesIO
import numpy as np
from matplotlib import pyplot as plt
from flask import Flask, send_file
from ipywidgets import interact, IntSlider
from ipywidgets.embed import embed_minimal_html


app = Flask(__name__)






def r2():
    x = np.random.uniform(0, 5, size=100)
    ep = np.random.normal(size=100)
    y = 2 * x + ep
    plt.scatter(x, y)
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


@app.route("/")
def hello():
    return r2()
    # fx = lambda x: x**2
    # interact_widget = interact(fx, x=IntSlider(min=0, max=100, step=1, value=10))
    # return embed_minimal_html('exported_interact.html', views=[interact_widget.widget],
    #                    state=interact_widget.widget.get_state())


if __name__=="__main__":
    app.run(debug=True)