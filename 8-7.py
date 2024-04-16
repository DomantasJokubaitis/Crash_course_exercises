def make_album(album, artist, num_songs = None):
    album_info = {"album" : album, "artist" : artist}

    if num_songs:
        album_info["number of songs"] = num_songs
    return album_info

info = make_album(album = "IWTDINO", artist = "Suicideboys", num_songs = 14)
print(info)
info = make_album(album = "Kill yourself part I", artist = "Suicideboys")
print(info)
info = make_album(album = "SSS", artist = "Suicideboys")
print(info)
