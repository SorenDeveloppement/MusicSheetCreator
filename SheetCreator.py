import SheetProperties
from helper import MSCXFileHeper as msc


class SheetCreator:
    def __init__(self, title: str, subtitle: str | None, author: str | None, instrument: SheetProperties | str | None, speed: int, key: SheetProperties, signature_nb: int, signature_type: SheetProperties, measure_nb: int, path: str):
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.instrument = instrument
        self.speed = speed
        self.key = key
        self.signature_nb = signature_nb
        self.signature_type = signature_type
        self.measure_nb = measure_nb
        self.path = path
        self.file = msc.MSCXFile(self.path)

    def setPartitionTitle(self, title: str):
        self.file.setTagValue("<metaTag name=\"workTitle\">", title)

    def setPartitionComposer(self, composer: str):
        self.file.setTagValue("<metaTag name=\"workTitle\">", composer)

    def setMeasureNb(self, nb: int):
        m = self.file.getMeasureCount()

        if m > nb:
            self.file.removeMeasure(m - nb)
        elif m < nb:
            self.file.addMeasure(nb - m)
        else:
            pass
