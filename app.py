from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission here!
        pass

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
