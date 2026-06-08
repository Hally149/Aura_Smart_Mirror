# backend

from flask import Flask, jsonify, request, render_template
from emotion_detection import detect_emotion
from spotify_music import get_song_for_emotion
from bs_detector import analyze_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')
 
@app.route('/api/emotion', methods=['POST'])
def emotion_api():
    image = request.files['image']
    emotion = detect_emotion(image)
    return jsonify({'emotion': emotion})

@app.route('/api/music', methods=['GET'])
def music_api():
    mood = request.args.get('mood')
    track = get_song_for_emotion(mood)
    return jsonify(track)

@app.route('/api/bs_detector', methods=['POST'])
def bs_api():
    text = request.json['text']
    result = analyze_text(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
  
# Copyright © 2026 Osasere H. Ero. All rights reserved.
# Proprietary and confidential. Unauthorized copying of this file, via any medium, is strictly prohibited.


