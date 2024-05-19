from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/live-coordinates')
def live_coordinates():
    # Simulate live coordinates for demonstration
    lat = 18.5434664
    lng = 73.7831388
    return jsonify(lat=lat, lng=lng)

if __name__ == '__main__':
    app.run(debug=True)
