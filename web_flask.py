from distutils.log import debug
from flask import Flask, render_template, jsonify
import get_data
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("base.html",)

@app.route("/artists")
def get_artists():
    artists = get_data.get_all_artist()
    artist_array = [{'id': i[0], 'name': i[1]} for i in artists]
    return jsonify(artist_array)

@app.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs= get_data.get_all_songs(aid)
    songs_array=[{'id': i[1], 'name': i[0]}for i in songs]
    # singer= get_data.singer(aid)
    # artists = get_data.get_all_artist()
    return jsonify(songs_array)
    # return render_template("songlist.html",artists=artists,songs=songs,singer=singer,active_artrist=aid)

@app.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid,aid):
    lyrics= get_data.get_lyrics(sid)
    songs= get_data.get_all_songs(aid)
    singer= get_data.singer(aid)
    artists = get_data.get_all_artist()
    print(lyrics)
    return jsonify(lyrics)
    # return render_template("lyrics.html",lyrics=lyrics,artists=artists,songs=songs,singer=singer,active_artrist=aid,active_song=sid)

if __name__=="__main__":
    app.run(debug=True) 