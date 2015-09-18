from flask import Flask, render_template
import getdata

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('main.html', coordinates = getdata.coordinates, 
    						concerts = getdata.concerts)

if __name__ == '__main__':
    app.run(debug=False)