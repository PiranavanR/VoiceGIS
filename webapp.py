from flask import Flask, render_template, request, jsonify
from VoiceRecognition import recognize
import webbrowser
app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice-command', methods=['POST'])
def voice_command():
    command = recognize()
    return jsonify({'command': command})

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=False)
