from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask import send_from_directory
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/images/<path:path>')
def images(path):
    return send_from_directory('images', path)

@app.route('/styles/<path:path>')
def styles(path):
    return send_from_directory('styles', path)

@app.route('/scripts/<path:path>')
def scripts(path):
    return send_from_directory('scripts', path)

@app.route('/')
def index():
    return render_template('teenmentalhealth.html')

@app.route('/chat')
def chat():
    return render_template('teenchat.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)