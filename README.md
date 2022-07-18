# lyric-chan

使用 FastAPI 构建的歌词 API ，支持从网易云音乐、Spotify 等平台获取歌词。

## Run

```bash
$ git clone https://github.com/fressive/lyric-chan
cd lyric-chan
```

复制 `config.sample.py` 到 `config.py` 并修改内容。

```bash
$ pip install -r requirements.txt
$ uvicorn app:app
```

如果想要指定服务监听地址，使用：
```bash
$ uvicorn app:app --host [address] --port [port]
```

## API Docs

[Here](API.md)

## TODO

- [] 配置节中增加 Spotify 代理支持
- [] 增加对 QQ 音乐的支持
- [] 增加对酷狗音乐的支持
- [] Cache

## Credits

Spotify 实现修改自 [akashrchandran/syrics](https://github.com/akashrchandran/syrics) (AGPL-3.0 license)。

## License

[MIT License](LICENSE)
