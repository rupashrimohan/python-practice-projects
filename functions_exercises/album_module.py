def make_album(artist, album_title, songs_count=None):
    """This function creates a music album dictionary"""
    music_album = {"artist": artist, "album_title": album_title}
    if songs_count:
        music_album["songs_count"] = songs_count
    return music_album
