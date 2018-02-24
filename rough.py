class myiter(object):
    def __init__(self, step):
        self.step = step
        print("Steps: " + str(self.step))

    def __next__(self):
        if self.step == 0:
            raise StopIteration        
        self.step -= 1
        return self.step

    def __iter__(self):
        return self

b = myiter(5)
for i in b:
    print(i)
