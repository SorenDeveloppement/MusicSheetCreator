import NoteProperties


class Note:
    def __init__(self, n_name: NoteProperties, n_type: NoteProperties, n_level: NoteProperties):
        self.name = n_name
        self.type = n_type
        self.level = n_level
