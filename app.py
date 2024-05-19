from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live-coordinates', methods=['POST'])
def live_coordinates():
    data = request.get_json()
    if not data or 'lat' not in data or 'lng' not in data:
        return jsonify({"error": "Invalid data"}), 400

    lat = data['lat']
    lng = data['lng']
    # Process the coordinates as needed, for now we just return them
    return jsonify(lat=lat, lng=lng)

if __name__ == '__main__':
    app.run(debug=True)
