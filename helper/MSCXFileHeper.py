
class MSCXFile:
    def __init__(self, path: str):
        self.path = path
        self.file = open(self.path, 'a')

    def readProperties(self):
        self.file.read().find()
