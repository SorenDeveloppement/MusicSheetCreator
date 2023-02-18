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

    def setTagValue(self, tag: str, value: int | str):
        out_file = []

        try:
            file = open(self.path, 'r')
            lines = file.readlines()

            for line in lines:
                if line.find(f"{tag}") != -1:
                    i = line.find(f"{tag}") + len(f"{tag}")
                    if len(line.split("><")) == 2:
                        out_file.append(line.split("><")[0] + f">{value}<" + line.split("><")[1])
                    else:
                        out_file.append(line.split("\">")[0] + f"\">{value}</" + line.split("</")[1])
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


# MSCXFile("../out/help/test.mscx").setTagValue("<metaTag name=\"composer\">", "Test")
