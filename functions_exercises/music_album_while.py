def make_album(artist, album_title, songs_count=None):
    """This function creates a music album dictionary"""
    music_album = {"artist": artist, "album_title": album_title}
    if songs_count:
        music_album["songs_count"] = songs_count
    return music_album


active = True
while active:
    artist = input("\nEnter the music artist name: ")
    album_title = input("Enter the album title: ")
    songs_count = input("Enter the songs count,(enter 'n' if you donot have): ")
    if songs_count.lower() == "n":
        album = make_album(artist, album_title)
    else:
        album = make_album(artist, album_title, songs_count)
    print(album)
    state = input("\nDo you want to continue('y'or'n'):")
    if state.lower() == "y":
        break
