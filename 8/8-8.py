def make_album(album, artist, num_songs = None):
    album_info = {"album" : album, "artist" : artist}

    if num_songs:
        album_info["number of songs"] = num_songs
    return album_info

while True:
    print(f"Press q to exit\n")

    
    album = input("Enter album: ")
    if album == "q":
        break
    artist = input("Enter artist: ")
    if artist == "q":
        break

    info = make_album(album, artist)
    print(info)
