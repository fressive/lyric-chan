import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from providers.spotify.api import Spotify

auth_manager = SpotifyClientCredentials(
                client_id=config.spotify_client_id,
                client_secret=config.spotify_client_secret
            )
sp = spotipy.Spotify(auth_manager=auth_manager)

client = Spotify(config.sp_dc)

def format_lrc(lyrics_json):
    lyrics = lyrics_json['lyrics']['lines']
    if lyrics_json['lyrics']['syncType'] == 'UNSYNCED':
        lrc = [lines['words'] for lines in lyrics]
    else:
        lrc = []
        for lines in lyrics:
            duration = int(lines['startTimeMs'])
            minutes, seconds = divmod(duration / 1000, 60)
            lrc.append(f'[{minutes:0>2.0f}:{seconds:.3f}] {lines["words"]}')
    return '\n'.join(lrc)

def fetch(title, artist, album):
    q = f"track:{title}"
    if artist:
        q += f" artist:{artist}"
    if album:
        q += f" album:{album}"
    query = sp.search(q=q, type="track", limit=config.spotify_track_limits)
    lyrics = []

    for i in query['tracks']["items"]:
        try:
            lyrics_json = client.get_lyrics(i['id'])
            lyrics.append({
                "source": format_lrc(lyrics_json),
                "zh_CN": None,
                "provider": "spotify",
                "title": i["name"],
                "artists": list(map(lambda x: x["name"], i["artists"])),
                "album": i["album"]["name"],
                "extra": {
                    "spotify_track_id": i['id'],
                    "spotify_album_id": i["album"]["id"],
                    "spotify_artists_id": dict(zip(map(lambda x: x["name"], i["artists"]), map(lambda x: x["id"], i["artists"])))
                }
            })
        except:
            continue

    return lyrics
