from bson import ObjectId
from fastapi import HTTPException
from database import collection

def serialize_song(song):
    return {
        "id": str(song["_id"]),
        "name": song["name"],
        "path": song["path"],
        "plays": song["plays"]
    }

def get_all_songs():
    return [serialize_song(song) for song in collection.find()]

def create_song(song_data):
    result = collection.insert_one(song_data.dict())
    return serialize_song(collection.find_one({"_id": result.inserted_id}))

def update_song(song_id, updates):
    result = collection.update_one({"_id": ObjectId(song_id)}, {"$set": updates.dict(exclude_unset=True)})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return serialize_song(collection.find_one({"_id": ObjectId(song_id)}))

def delete_song(song_id):
    result = collection.delete_one({"_id": ObjectId(song_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Canción no encontrada")
    return {"message": "Canción eliminada correctamente"}