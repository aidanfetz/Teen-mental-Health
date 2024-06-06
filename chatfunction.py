from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, send
from flask import send_from_directory

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
@app.route('/templates/<path:path>')
def templates(path):
    return send_from_directory('templates', path)


@app.route('/')
def index():
    return render_template('teenmentalhealth.html')

@app.route('/teenchat.html')
def chat():
    return render_template('teenchat.html')

@socketio.on('message')
def handle_message(msg):

    msg1 = str(msg).lower()
    msgli = str(msg1).split()

    if "fuck" in msgli:
        print('Message bad: ' + str(msg1))
        print("------------")
    
    elif "shit" in msgli:
        print('Message bad: ' + str(msg1))
        print("------------")

    elif "bitch" in msgli:
        print('Message bad: ' + str(msg1))
        print("-----------")

    elif "pussy" in msgli:
        print('Message bad: ' + str(msg1))
        print("-----------")

    elif "cunt" in msgli:
        print('Message bad: ' + str(msg1))
        print("-----------")

    elif "hoe" in msgli:
        print('Message bad: ' + str(msg1))
        print("-----------")

    elif "nigger" in msgli:
        print('Message bad: ' + str(msg1))
        print("-----------")
    
    elif "beaner" in msgli:
        print('Message bad: ' + str(msg1))
        print("-----------")

    elif "whore" in msgli:
        print('Message bad: ' + str(msg1))
        print("-----------")

   

    elif "address" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)
    elif "phone" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif "number" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif "jerk" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)
    
    elif "off" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif "sex" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif "whole" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif "hole" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif "in" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif "niger" in msgli:
        print('Message flagged: ' + str(msg1))
        print('~~~~~~~~~~~~~~~~')
        send(msg, broadcast=True)

    elif msg1 == " ":
        print("No Message")
        print("**********")
    
    elif msg1 == "":
        print("No Message")
        print("**********")

    else:
        print('Message: ' + str(msg1))
        send(msg, broadcast=True)

userlist = []

@app.route('/user', methods = ['POST'])
def handle_user():
    user = request.json
    if user['name'] == "bad":
        print('bad user: ' + user['name'])
        raise Exception("bad user: " + user['name'])
    if user['name'] + "//" + user['password'] in userlist:
        print('returning user:  ' + user['name'] + "//" + user['password'])
        return jsonify({'username':user['name']})
    else:
        userlist.append(user['name'] + "//" + user['password'])
        print("new user:  " + user['name'] + "//" + user['password'])
        return jsonify({'username':user['name']})
    
@app.route("/IP", methods = ["GET"])
def handle_IP():
    IP = request.json
    return jsonify({"IP":IP['IP']})

if __name__ == '__main__':
    socketio.run(app)