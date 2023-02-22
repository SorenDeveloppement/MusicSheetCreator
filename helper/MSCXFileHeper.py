import NoteProperties


class MSCXFile:
    def __init__(self, path: str):
        self.path = path

    def getTagValueByName(self, tagname: str) -> str:
        tagValue = ""

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find(f"{tagname}") != -1:
                    i = line.find(f"name=\"{tagname}\">") + len(f"name=\"{tagname}\">")
                    while line[i] != "<":
                        tagValue += line[i]
                        i += 1
                    break

            file.close()
        except Exception as e:
            print("No value found", f"\r {e}")

        return tagValue

    def getTagValue(self, tagname: str) -> str:
        tagValue = ""

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find(f"{tagname}") != -1:
                    i = line.find(f"<{tagname}>") + len(f"<{tagname}>")
                    while line[i] != "<":
                        tagValue += line[i]
                        i += 1
                    break

            file.close()
        except Exception as e:
            print("No value found", f"\r {e}")

        return tagValue

    @staticmethod
    def getValue(tag: str) -> str:
        tagValue = ""

        i = tag.find(">") + 1
        while tag[i] != "<":
            tagValue += tag[i]
            i += 1

        return tagValue

    def setTagValue(self, tag: str, value: int | str):
        out_file = []

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find(f"{tag}") != -1:
                    if len(line.split("><")) == 2:
                        out_file.append(line.split("><")[0] + f">{value}<" + line.split("><")[1])
                    else:
                        out_file.append(line.split(">")[0] + f">{value}</" + line.split("</")[1])
                else:
                    out_file.append(line)

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

        except Exception as e:
            print(e)

    def getTitle(self) -> str:
        title = ""

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find("workTitle") != -1:
                    i = line.find("name=\"workTitle\">") + len("name=\"workTitle\">")
                    while line[i] != "<":
                        title += line[i]
                        i += 1
                    break

            file.close()
        except Exception as e:
            print("No value found", f"\r {e}")

        return title

    def getComposer(self) -> str:
        composer = ""

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find("composer") != -1:
                    i = line.find("name=\"composer\">") + len("name=\"composer\">")
                    while line[i] != "<":
                        composer += line[i]
                        i += 1
                    break

            file.close()
        except Exception as e:
            print("No value found", f"\r {e}")

        return composer

    def getMeasureCount(self) -> int:
        count = 0

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find("<Measure>") != -1:
                    count += 1

            file.close()
        except Exception as e:
            print("No measure in your partition", f"\r{e}")

        return count

    def getNoteCount(self) -> int:
        count = 0

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find("<Note>") != -1:
                    count += 1

            file.close()
        except Exception as e:
            print("No note in your partition", f"\r{e}")

        return count

    def getTimeSignature(self) -> str:
        return self.getTagValue("sigN") + '/' + self.getTagValue("sigD")

    def setTimeSignature(self, sig: str):
        time_sig = sig.split('/')
        self.setTagValue("sigN", time_sig[0])
        self.setTagValue("sigD", time_sig[1])
        out_file = []

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find("duration") != -1 and line.find("durationType") == -1:
                    if not self.getTagValue("duration") == sig:
                        print(line)
                        out_file.append(f"\t\t\t<duration>{sig}</duration>\r")
                else:
                    out_file.append(line)

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

        except Exception as e:
            print(e)

    def getTempo(self) -> str:
        tempo = ""

        tagValue = ""
        try:
            file = open(self.path, 'r')
            lines = file.readlines()
            li = 0

            for line in lines:
                if line.find("text") != -1 and lines[li + 1].find("</Tempo>") != -1:
                    i = line.find("<text>") + len("<text>")
                    while line.find("</text>") != i:
                        tagValue += line[i]
                        i += 1
                    break
                li += 1

            file.close()
        except Exception as e:
            print("No value found", f"\r {e}")

        for i in tagValue:
            if i.isdigit():
                tempo += i

        return tempo

    def setTempo(self, tempo: int):
        tagValue = ""
        try:
            file = open(self.path, 'r')
            lines = file.readlines()
            li = 0
            out_file = []

            for line in lines:
                if line.find("tempo") != -1 and lines[li - 1].find("<Tempo>") != -1:
                    out_file.append(f"\t\t\t<tempo>{tempo/60:.5f}</tempo>\r")
                elif line.find("text") != -1 and lines[li + 1].find("</Tempo>") != -1:
                    out_file.append(f"\t\t\t<text><sym>metNoteQuarterUp</sym> = {tempo}</text>\r")
                else:
                    out_file.append(line)
                li += 1

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

        except Exception as e:
            print("No value found", f"\r {e}")


    def addMeasure(self, count: int, duration: str = "4/4"):
        xml = f"\t<Measure>\r\t\t<voice>\r\t\t\t<Rest>\r\t\t\t\t<durationType>measure</durationType>\r\t\t\t\t\t<duration>{duration}</duration>\r\t\t\t\t</Rest>\r\t\t\t</voice>\r\t\t</Measure>\r"
        out_file = []

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            li = 0
            for line in lines:
                out_file.append(line)
                li += 1
                if li + 1 >= len(lines):
                    continue
                else:
                    if (lines[li].find("</Staff>") != -1) & (lines[li - 1].find("</Measure>") != -1):
                        for i in range(count):
                            out_file.append(xml)

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

        except Exception as e:
            print(e)

    def removeMeasure(self, count: int):
        out_file = []
        found = False

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            c = 1
            m_found = 0
            li = 0
            for line in lines:
                if line.find("<Measure>") != -1:
                    m_found += 1
                    if self.getMeasureCount() - m_found <= count:
                        if c <= count:
                            found = True
                        else:
                            found = False
                        c += 1

                if found:
                    pass
                else:
                    out_file.append(line)

                li += 1

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

        except Exception as e:
            print(e)

    def addNote(self, note: NoteProperties, duration: NoteProperties, measure: int):
        xml = f"\t\t  <Chord>\r\t\t\t<durationType>{duration}</durationType>\r\t\t\t  <Note>\r\t\t\t\t<pitch>{note[1]}</pitch>\r\t\t\t\t<tpc>{note[2]}</tpc>\r\t\t\t  </Note>\r\t\t\t</Chord>\r"
        out_file = []
        f = False
        f2 = False
        li = 0

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            m_found = 0
            for line in lines:

                if line.find("<Rest>") != -1:
                    if m_found == measure:
                        f = True
                if line.find("</voice>") != -1:
                    if m_found == measure:
                        f = False

                if f:
                    pass
                else:
                    out_file.append(line)

                if line.find("<Measure>") != -1:
                    m_found += 1
                if m_found == measure:
                    if not li + 1 == len(lines):
                        if lines[li + 1].find("</voice>") != -1:
                            print("2 - OK")
                            out_file.append(xml)

                li += 1

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

            self.verifyMeasureNoteCount(measure)

        except Exception as e:
            print(e)

    def addNotes(self, *args: [NoteProperties, NoteProperties], measure: int):
        out_file = []
        f = False
        f2 = False
        li = 0

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            m_found = 0
            for line in lines:

                if line.find("<Rest>") != -1:
                    if m_found == measure:
                        f = True
                if line.find("</voice>") != -1:
                    if m_found == measure:
                        f = False

                if f:
                    pass
                else:
                    out_file.append(line)

                if line.find("<Measure>") != -1:
                    m_found += 1
                if m_found == measure:
                    if not li + 1 == len(lines):
                        if lines[li + 1].find("</voice>") != -1:
                            for note in args:
                                if note[0] == NoteProperties.REST:
                                    xml = f"\t\t  <Rest>\r\t\t\t<durationType>{note[1]}</durationType>\r\t\t\t</Rest>\r"
                                    out_file.append(xml)
                                else:
                                    xml = f"\t\t  <Chord>\r\t\t\t<durationType>{note[1]}</durationType>\r\t\t\t  <Note>\r\t\t\t\t<pitch>{note[0][1]}</pitch>\r\t\t\t\t<tpc>{note[0][2]}</tpc>\r\t\t\t  </Note>\r\t\t\t</Chord>\r"
                                    out_file.append(xml)

                li += 1

            with open('out.mscx', 'w') as f:
                f.writelines(out_file)
                f.close()

            self.verifyMeasureNoteCount(measure)

        except Exception as e:
            print(e)

    def verifyMeasureNoteCount(self, measure: int):
        try:
            file = open(self.path, 'r')
            lines = file.readlines()
            timeSignature = int(self.getTagValue("sigN"))
            timefound = 0

            m_found = 0

            for line in lines:
                if line.find("<Measure>") != -1:
                    m_found += 1

                if m_found == measure:
                    if line.find("<durationType>") != -1:
                        if self.getValue(self, line) == "32nd":
                            timefound += 1 / 8
                        elif self.getValue(self, line) == "16th":
                            timefound += 1 / 4
                        elif self.getValue(self, line) == "heighth":
                            timefound += 1 / 2
                        elif self.getValue(self, line) == "quarter":
                            timefound += 1
                        elif self.getValue(self, line) == "half":
                            timefound += 2
                        elif self.getValue(self, line) == "whole":
                            timefound += 4

            if timefound > timeSignature:
                print(
                    f"\033[91m Too many time in measure {measure} ! Found {timefound:.2f} instead {timeSignature}.\033[00m")

        except Exception as e:
            print(e)


"""print(MSCXFile("out.mscx").getTempo())
MSCXFile("out.mscx").setTempo(90)"""
