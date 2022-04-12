from flask import Blueprint, jsonify
import get_data

api = Blueprint('api', __name__)

@api.route("/artist")
def get_artists():
    artists = get_data.get_all_artist()
    artist_array = [{'id': i[0], 'name': i[1]} for i in artists]
    return jsonify(artist_array)
    # return jsonify({"name": "Shahina"})

@api.route("/songs/<int:aid>")
def list_all_songs(aid):
    songs= get_data.get_all_songs(aid)
    songs_array=[{'id': i[1], 'name': i[0]}for i in songs]
    # singer= get_data.singer(aid)
    # artists = get_data.get_all_artist()
    return jsonify(songs_array)
    # return render_template("songlist.html",artists=artists,songs=songs,singer=singer,active_artrist=aid)

@api.route("/songs/<int:aid>/lyrics/<int:sid>")
def lyrics(sid,aid):
    lyrics= get_data.get_lyrics(sid)
    songs= get_data.get_all_songs(aid)
    singer= get_data.singer(aid)
    artists = get_data.get_all_artist()
    # print(lyrics)
    return jsonify(lyrics)
    # return render_template("lyrics.html",lyrics=lyrics,artists=artists,songs=songs,singer=singer,active_artrist=aid,active_song=sid)
   