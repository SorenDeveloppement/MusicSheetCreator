import SheetProperties


class SheetCreator:
    def __init__(self, title: str, subtitle: str | None, author: str | None, instrument: SheetProperties | str | None, speed: int, key: SheetProperties, signature_nb: int, signature_type: SheetProperties):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.instrument = instrument
        self.speed = speed
        self.key = key
        self.signature_nb = signature_nb
        self.signature_type = signature_type
