from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__) # Initialize Flask app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        state = request.form.get('state')
        urgency = request.form.get('urgency')
        severity = request.form.get('severity')
        certainty = request.form.get('certainty')
        max_results = request.form.get('max_results')

        # Make the NOAA API request and process the results
        url = f'https://api.weather.gov/alerts?active=true&status=actual&message_type=alert&area={state}&urgency={urgency}&severity={severity}&certainty={certainty}&limit={max_results}'
        # ...

        return render_template('results.html', alerts=alerts)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
