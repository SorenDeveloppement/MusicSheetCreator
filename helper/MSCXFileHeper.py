
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
        except Exception as e:
            print("No value found", f"\r {e}")

        return tagValue

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
        except Exception as e:
            print("No value found", f"\r {e}")

        return composer


"""
print(MSCXFile("../out/help/test.mscx").getTitle())
print(MSCXFile("../out/help/test.mscx").getComposer())
print(MSCXFile("../out/help/test.mscx").getTagValue("longName"))
print(MSCXFile("../out/help/test.mscx").getTagValueByName("creationDate"))
print(MSCXFile("../out/help/test.mscx").getTagValueByName("composer"))
"""
