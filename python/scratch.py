class myDict:
    def __init__(self):
        self._dict = {}

    def add(self, id, val):
        self._dict[id.lower()] = val

    def return_all(self):
        return self._dict


md = myDict()
md.add('ID', 123)
print(md.return_all())