# Class file for species type

class Species:
    def __init__(self, *args):
        self.__dict__.update(*args)      

    def getImage(self):
        return self.image
