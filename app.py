from fastapi import FastAPI

from fetch_lyric import fetch_lyric

app = FastAPI()

@app.get("/api/v1/lyrics")
def lyric(title: str, artist: str = "", album: str = "", fastmode: bool = False):
    return {"response": 200, "data": fetch_lyric(title, artist, album, fastmode)}