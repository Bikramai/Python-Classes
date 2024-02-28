class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):#incapsulating casesensitivity in a tag
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)

cloud = TagCloud()
# print(cloud.__tags) #private members
# cloud["python"] = 10
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.__tags["PYTHON"])
print(cloud.__dict__)