import SheetProperties
from helper import MSCXFileHeper as msc


class SheetCreator:

    def __init__(self, title: str, composer: str, instrument: SheetProperties | str | None,
                 tempo: int, key: SheetProperties, signature_nb: int, signature_type: SheetProperties, measure_nb: int,
                 path: str, musescore_version: int):
        self.title = title
        self.composer = composer
        self.instrument = instrument
        self.tempo = tempo
        self.key = key
        self.signature_nb = signature_nb
        self.signature_type = signature_type
        self.measure_nb = measure_nb
        self.path = path
        self.file = msc.MSCXFile(self.path)
        self.ms_v = musescore_version

    def createPartition(self):
        try:
            out_file = [line for line in open("helper/template.mscx").readlines()]

            with open(self.getPath(), 'w') as f:
                f.writelines(out_file)
                f.close()

            self.setPartitionTitle(self.title)
            self.setPartitionComposer(self.composer)
            self.setMeasureNb(self.measure_nb)

        except Exception as e:
            print(e)

    def setPartitionTitle(self, title: str):
        self.file.setTagValue("<metaTag name=\"workTitle\">", title)
        try:
            lines = open(self.path).readlines()
            out_file = []
            li = 0

            for line in lines:
                if lines[li - 1].find("<style>Title</style>") != -1:
                    print("OK")
                    out_file.append(f"\t\t  <text>{title}</text>\r")
                else:
                    out_file.append(line)
                li += 1

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

        except Exception as e:
            print(e)

    def setPartitionComposer(self, composer: str):
        self.file.setTagValue("<metaTag name=\"composer\">", composer)
        try:
            lines = open(self.path).readlines()
            out_file = []
            li = 0

            for line in lines:
                if lines[li - 1].find("<style>Composer</style>") != -1:
                    print("OK")
                    out_file.append(f"\t\t  <text>{composer}</text>\r")
                else:
                    out_file.append(line)
                li += 1

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

        except Exception as e:
            print(e)

    def setMeasureNb(self, nb: int):
        m = self.file.getMeasureCount()

        if m > nb:
            self.file.removeMeasure(m - nb)
        elif m < nb:
            self.file.addMeasure(nb - m)
        else:
            pass

    def getPath(self) -> str:
        return self.path
