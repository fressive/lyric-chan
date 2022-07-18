""" APP 配置 """

lyric_providers = ["netease", "spotify"]
# 启用的歌词提供者
# 注意：spotify 可能在国内无法正常使用。

""" Netease """

netease_track_limits = 3
# 网易云最大返回搜索结果数目。数值越小 API 响应越快。

""" Spotify """

sp_dc = ""
# spotify.com 上的 Cookie `sp_dc` 

spotify_client_id = "3eddf8157ce94c75a412a4cd84507bbb"
spotify_client_secret = "f1c5e360699b444d867524c4ecaedbeb"
# Spotify Client Settings
# From https://github.com/akashrchandran/syrics

spotify_track_limits = 3
# Spotify 最大返回搜索结果数目。数值越小 API 响应越快。
