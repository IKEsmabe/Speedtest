from flask import Flask, render_template, jsonify
import speedtest as st

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speedtest')
def speedtest():
    test = st.Speedtest()
    down_speed = round(test.download() / 10**6, 2)
    up_speed = round(test.upload() / 10**6, 2)
    ping = test.results.ping
    return jsonify({'download_speed': down_speed, 'upload_speed': up_speed, 'ping': ping})

if __name__ == '__main__':
    app.run(debug=True)