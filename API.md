# API Document

## 获取歌词

**GET** `/api/v1/lyrics`

请求

- `title`* string: 歌曲标题
- `artist` string: 艺术家
- `album` string: 专辑
- `fastmode` bool: 启用快速模式（开启后只会从首选的歌词提供者中获取歌词），默认为 `false`

响应

```
/api/v1/lyrics?title=days (Re Ver.)&artist=Jin
```

```json
{
    "response": 200,
    "data": [
        {
            "source": "[00:10.28]意味のないままで 時間は過ぎて\n[00:20.09]理解しようとして 気付いた\n...",
            "zh_CN": "...",
            "provider": "netease",
            "title": "days (Re Ver.)",
            "artists": [
                "じん",
                "Lia"
            ],
            "album": "MEKAKUCITY M's MEKAKUCITY ACTORS VOCAL & SOUND COLLECTION",
            "extra": {
                "netease_song_id": 31260701,
                "netease_album_id": 3115587,
                "netease_artists_id": {
                    "じん": 160038,
                    "Lia": 16993
                }
            }
        },
        {
            "source": "[00:11.188] 意味のないままで時間は過ぎて\n[00:21.465] 理解しようとして気付いた\n....",
            "zh_CN": null,
            "provider": "spotify",
            "title": "Days - Re Ver.",
            "artists": [
                "Jin",
                "Lia"
            ],
            "album": "Mekakucity M's 2 ~Mekakucity Actors Vocal & Sound Collection~",
            "extra": {
                "spotify_track_id": "2clXNIYMyjFD1jHIbAyklh",
                "spotify_album_id": "3SSYinciPEWb4y9V6HOS6m",
                "spotify_artists_id": {
                    "Jin": "7to1UlTpu40h7CpjRPkGqA",
                    "Lia": "1ST32ORsxC2Huh5FdSWelw"
                }
            }
        },
        {
            "source": "[00:11.025] 意味のないままで　時間は過ぎて\n[00:20.846] 理解しようとして　気付いた\n...",
            "zh_CN": null,
            "provider": "spotify",
            "title": "days - Re Ver.",
            "artists": [
                "Jin",
                "Lia"
            ],
            "album": "Songs to Fly",
            "extra": {
                "spotify_track_id": "1cCtRx6XRNfflJExLNLJJB",
                "spotify_album_id": "1R00XIFJlfIvfmvrnQw8GF",
                "spotify_artists_id": {
                    "Jin": "7to1UlTpu40h7CpjRPkGqA",
                    "Lia": "1Z0sSjjlCFNG4WvU0DUG8t"
                }
            }
        }
    ]
}
```