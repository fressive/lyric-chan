import config

import providers.netease
import providers.spotify

providers = {
    "netease": providers.netease.fetch,
    "spotify": providers.spotify.fetch
}

def fetch_lyric(title, artist, album, fastmode = False):
    lyrics = []

    for i in config.lyric_providers:
        data = providers[i](title, artist, album)
        
        if data and len(data) != 0:
            lyrics = lyrics + data

            if fastmode:
                break

    return lyrics