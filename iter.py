class countdown(object):
    def __init__(self, start):
        self.counter = start + 1
    def __next__(self):
        self.counter -= 1
        if self.counter <= 0:
            raise StopIteration
        return self.counter
    def __iter__(self):
        return self
