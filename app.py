from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

NASA_API_KEY = '5doj8kpbe88fbkRylonOYK1br6CqhYtVRbV92zEJ'  # Use a chave DEMO para testes iniciais. Recomendo obter sua própria chave mais tarde.

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch-Image/<date>', methods=['GET'])
def fetch_image(date):
    APOD_URL = f'https://api.nasa.gov/planetary/apod?date={date}&api_key={NASA_API_KEY}'
    response = requests.get(APOD_URL)
    if response.status_code == 200:
        data = response.json()
        
        return jsonify(data)
    else:
        
        return jsonify({"error":"Failed to fetch image"})
    
if __name__ == '__main__':
    app.run(debug=True)

