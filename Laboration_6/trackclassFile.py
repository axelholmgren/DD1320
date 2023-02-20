class track:
    def __init__(self, trackid, låttid, artistnamn, låttitel):
        self.trackid = trackid
        self.låttid = låttid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn
