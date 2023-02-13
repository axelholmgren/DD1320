""" Klass med två attribut. Ett word som är ordet 
och en parent som är föräldet till ordet. """

class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent
