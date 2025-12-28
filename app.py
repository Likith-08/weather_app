from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "f8c9f93c556fe8a93cc6ce9ffcf38a1b"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.json['city']
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data['cod'] != 200:
        return jsonify({"error": "City not found"})

    weather_data = {
        "city": data['name'],
        "temp": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "wind": data['wind']['speed'],
        "condition": data['weather'][0]['description']
    }

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
