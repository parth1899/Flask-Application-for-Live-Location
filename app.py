from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Global variable to store the latest coordinates
latest_coords = {'lat': 18.5434664, 'lng': 73.7831388}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live-coordinates', methods=['POST', 'GET'])
def live_coordinates():
    global latest_coords
    if request.method == 'POST':
        data = request.get_json()
        if not data or 'lat' not in data or 'lng' not in data:
            return jsonify({"error": "Invalid data"}), 400
        latest_coords = {'lat': data['lat'], 'lng': data['lng']}
        return jsonify(lat=latest_coords['lat'], lng=latest_coords['lng'])
    else:
        return jsonify(lat=latest_coords['lat'], lng=latest_coords['lng'])

if __name__ == '__main__':
    app.run(debug=True)
