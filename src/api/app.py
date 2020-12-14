"""Music for humans is a project to reverse engineer spotify, and maybe make it less evil along the way."""

from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Test to make sure flask works as expected."""
    return "Hello, World!"


@app.route("/music/<song_name>")
def stream_song(song_name):
    """Stream a song at music/song_name."""
    def generate():
        with open(f"music/{song_name}.wav", "rb") as songfile:
            data = songfile.read(1024)
            while data:
                yield data
                data = songfile.read(1024)
    return Response(generate(), mimetype="audio/wav")

