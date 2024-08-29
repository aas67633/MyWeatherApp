from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = '069ffabe4810b705c570534f6a2acc73'  # Replace with your actual API key

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    city = request.args.get('city', '')
    weather = None
    if city:
        weather = get_weather(city)
    return render_template('index.html', weather=weather, city=city)

if __name__ == '__main__':
    app.run(debug=True)

