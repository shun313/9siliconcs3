class MusicTrack:
    def __init__(self, title, genre, artist, isBlocked):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.__isBlocked = isBlocked

    def play(self):
        print(f"Playing: {self.title}")

    def blockArtist(self):
        self.__isBlocked = True
        print(f"{self.artist} has been blocked.")

    def showLyrics(self):
        print(f"Showing lyrics for: {self.title}")

    def get_isBlocked(self):
        return self.__isBlocked


class Playlist:
    def __init__(self, name, creator):
        self.name = name
        self.creator = creator
        self.tracks = []

    def addTrack(self, track):
        self.tracks.append(track)
        print(f"Added '{track.title}' to the playlist.")

    def showTracks(self):
        print(f"\nPlaylist: {self.name}")
        print(f"Created by: {self.creator}")
        print("Tracks:")

        for track in self.tracks:
            print(f"- {track.title} by {track.artist}")


playlist1 = Playlist("Top songs ko", "Shun")

song1 = MusicTrack("Street by street", "Jazz", "Laufey", False)
song2 = MusicTrack("Heavy Serenade", "Kpop", "Nmixx", False)
song3 = MusicTrack("Noypi", "Rock", "Bamboo", False)


print("Before association:")
print(f"Playlist: {playlist1.name}")
print("Tracks:", playlist1.tracks)


print("\nBuilding association")
playlist1.addTrack(song1)
playlist1.addTrack(song2)
playlist1.addTrack(song3)


print("\nAfter association")
playlist1.showTracks()
