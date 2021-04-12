class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.count = len(dictionary) - 1
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.count:
            keys = list(self.dictionary.keys())
            values = list(self.dictionary.values())
            self.start += 1
            return keys[self.start], values[self.start]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
