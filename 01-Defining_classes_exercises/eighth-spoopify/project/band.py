# from song import Song
# from album import Album

class Band:
    def __init__(self, name):
        self.name = name
        self.albums = list()

    def add_album(self, album): # Album
        if album.name in [el.name for el in self.albums]:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in [el.name for el in self.albums]:
            return f"Album {album_name} is not found."
        if album_name in [el.name for el in self.albums if el.published == True]:
            return f"Album has been published. It cannot be removed."
        self.albums = [album for album in self.albums if album.name != album_name]
        return f"Album {album_name} has been removed."

    def details(self):
        result_band = "Band " + self.name + "\n"
        result_band += "".join([el.details() for el in self.albums])
        return result_band


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
