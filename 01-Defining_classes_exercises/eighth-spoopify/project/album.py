# from song import Song

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):  # -> Song
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in self.songs:
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(song_name)
        return f"Removed song {song_name} from album {self.name}"

    def publish(self):
        if not self.published:
           self.published = True
           return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = f"Album {self.name}\n"+"".join([f"== {el.get_info()}\n" for el in self.songs])
        return result

# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# print(album.details())

