from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def callback():
    return send_file('static/iris.html')

if __name__ == '__main__':
    app.run('localhost', port=80)
