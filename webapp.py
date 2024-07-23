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

    
  
