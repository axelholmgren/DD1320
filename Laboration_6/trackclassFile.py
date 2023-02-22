class Track:
    # Class som sparar låtarna med attribut för varje del av låtarna
    def __init__(self, trackid, låttid, artistnamn, låttitel):
        self.trackid = trackid
        self.låttid = låttid
        self.artistnamn = artistnamn
        self.låttitel = låttitel

    def __lt__(self, other):
        # Lt metod för att kunna sortera låtarna
        return self.låttitel < other.låttitel
