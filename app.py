from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

us_states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        state = request.form['state']
        urgency = request.form['urgency']
        severity = request.form['severity']
        certainty = request.form['certainty']
        max_results = int(request.form['max_results'])

        params = {
            'active': 'true',
            'status': 'actual',
            'message_type': 'alert',
            'area': state,
            'urgency': urgency,
            'severity': severity,
            'certainty': certainty
        }

        response = requests.get("https://api.weather.gov/alerts", params=params, headers={'User-Agent': 'myweatherapp'})
        data = response.json()
        alerts = data['features'][:max_results]

        return jsonify(alerts)

    return render_template("index.html", us_states=us_states)

if __name__ == "__main__":
    app.run(debug=True)
