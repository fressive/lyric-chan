import config
import requests
from NetEaseMusicApi import api

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54"

def fetch(title, artist, album):
    songs = api.search.songs("{} {} {}".format(artist, album, title))

    lyrics = []

    if not songs:
        return None

    n = 0

    for i in songs:
        if n >= config.netease_track_limits:
            break

        if not i["name"].lower() == title.lower():
            continue
        
        song_id = i["id"]
        data = requests.get("http://music.163.com/api/song/lyric?os=osx&id={}&lv=-1&kv=-1&tv=-1".format(song_id), headers={"User-Agent": user_agent}).json()

        if not "lrc" in data.keys():
            continue
        
        lyric = data["lrc"]["lyric"]

        if "tlyric" in data.keys():
            translated_lyric = data["tlyric"]["lyric"]
            
        lyrics.append({
            "source": lyric,
            "zh_CN": translated_lyric,
            "provider": "netease",
            "title": i["name"],
            "artists": list(map(lambda x: x["name"], i["artists"])),
            "album": i["album"]["name"],
            "extra": {
                "netease_song_id": i["id"],
                "netease_album_id": i["album"]["id"],
                "netease_artists_id": dict(zip(map(lambda x: x["name"], i["artists"]), map(lambda x: x["id"], i["artists"])))
            }
        })

        n += 1

    return lyrics