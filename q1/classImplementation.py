class MusicTrack:
    def __init__(self, title, genre, artist, isBlocked):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.__isBlocked = isBlocked

    def play(self):
        print(self.title, "is now playing.")

    def blockArtist(self):
        self.__isBlocked = True
        print(self.artist, "has been blocked.")

    def showLyrics(self):
        print("Showing lyrics for", self.title)

    def get_isBlocked(self):
        return self.__isBlocked


object1 = MusicTrack("Street by street", "Jazz", "Laufey", False)
object2 = MusicTrack("Heavy Serenade", "Kpop", "Nmixx", False)


print("before:")
print("Object 1:", object1.title, "|", object1.genre, "|",
      object1.artist, "| Blocked:", object1.get_isBlocked())

print("Object 2:", object2.title, "|", object2.genre, "|",
      object2.artist, "| Blocked:", object2.get_isBlocked())


print("\nBlocking Object 1's artist...")
object1.blockArtist()


print("\nafter:")
print("Object 1:", object1.title, "|", object1.genre, "|",
      object1.artist, "| Blocked:", object1.get_isBlocked())

print("Object 2:", object2.title, "|", object2.genre, "|",
      object2.artist, "| Blocked:", object2.get_isBlocked())
