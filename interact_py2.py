from ipywidgets import interact, IntSlider
from ipywidgets.embed import embed_minimal_html

def f(x):
    return x ** 2

interact_widget = interact(f, x=IntSlider(min=0, max=100, step=1, value=10))
embed_minimal_html('exported_interact.html', views=[interact_widget.widget], state=interact_widget.widget.get_state())