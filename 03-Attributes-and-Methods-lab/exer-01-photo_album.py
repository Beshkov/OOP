import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(pages=math.ceil(photos_count / 4))

    def add_photo(self, label):
        for idx, p in enumerate(self.photos):
            if len(p) < 4:
                p.append(label)
                return f'"{label} photo added successfully on page {idx + 1} slot {len(p)}'
        return 'No more free spots'

    def display(self):
        result = ""
        for page in range(self.pages):
            result += '-' * 11 + '\n'
            result += ' '.join(['[]' for _ in self.photos[page]]) + '\n'

        result += '-' * 11 + '\n'
        return result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))

print(album.display())
