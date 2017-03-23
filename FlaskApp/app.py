from flask import Flask, render_template, request, make_response
import _pickle as pickle
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
from IPython.html.widgets import interact


app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')
@app.route("/about", methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')

@app.route('/plot.png')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    
    cost = 51775
    recidivism = 0.278
    xs =[1,2,3]
    ys = [i * cost * recidivism for i in xs]
    
    ppep_recidivism = 0.078
    y2 = [i * cost* ppep_recidivism for i in xs]
    

    axis.plot(xs, ys)
    axis.plot(xs, y2)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
    

if __name__ == "__main__":
    app.run(debug=True)

