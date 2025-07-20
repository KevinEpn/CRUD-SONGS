from fastapi import FastAPI
from models import Song, SongUpdate
import crud

app = FastAPI()

@app.get("/songs")
def get_songs():
    return crud.get_all_songs()

@app.post("/songs", status_code=201)
def add_song(song: Song):
    return crud.create_song(song)

@app.put("/songs/{song_id}")
def edit_song(song_id: str, updates: SongUpdate):
    return crud.update_song(song_id, updates)

@app.delete("/songs/{song_id}", status_code=204)
def remove_song(song_id: str):
    crud.delete_song(song_id)
    return