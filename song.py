Class Song:
    'A class for mp3 songs that modifies ID3v2 tags'

    def __init__(self, name=None, artist=None,track_number=None, album=None, \
                 genre=None, length=None):
        self.name = name
        self.artist = artist
        self.track_number = track_number
        self.album = album
        self.genre = genre
        self.length = length

    def set_name(new_name):
        'Sets the name ID3v2 tag by taking a new name as an argument'
        self.name = new_name

    def get_name():
        'Gets the name IDv2 tag and returns it as an argument'
        return self.name

    def show_mp3():
        'Displays all of the values for the song in a readable format'
        print("---{0}---".format(self.name))
        print("Artist: {0}".format(self.artist))
        print("Track #: {0}".format(self.track_number))
        print("Album: {0}".format(self.album))
        print("Genre: {0}".format(self.genre))
        print("Length: {0}".format(self.length))
