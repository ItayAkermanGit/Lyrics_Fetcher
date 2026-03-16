from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/get-lyrics", methods=["POST"])
def get_lyrics():
    data = request.get_json()

    if not data or "artist" not in data or "title" not in data:
        return jsonify({"error": "Missing artist or title"}), 400
    
    artist = data["artist"]
    title = data["title"]

    try:
        url = f"http://api.lyrics.ovh/v1/{artist}/{title}"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "Lyrics not found"}), 404
        
        lyrics = response.json().get("lyrics")

        return jsonify({
            "artist": artist,
            "title": title,
            "lyrics": lyrics
        })
    
    except Exception as e:
        return jsonify({"error": "Failed to fetch lyrics"}), 500
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)