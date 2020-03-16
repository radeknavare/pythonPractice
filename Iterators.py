class Reverse:
    def __init__(self, sdata):
        self.sdata = sdata
        self.len = len(self.sdata)

    def __iter__(self):
        return self

    def __next__(self):
        if self.len == 0:
            raise StopIteration
        self.len = self.len - 1
        return self.sdata[self.len]


r = Reverse("Kedar")
iter(r)
for char in r:
    print(char)


class OddNumbers:
    def __init__(self, number):
        self.number = number
        self.counter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.number:
            raise StopIteration
        else:
            self.counter += 2
            return self.counter


on = OddNumbers(10)
iter(on)
for i in on:
    print(i)
