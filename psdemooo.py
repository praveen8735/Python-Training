def compute(a, b):
    return a + b

class Demo:

    def __init__(self):
        self.demo = compute


d = Demo()
print(d.demo(12, 33))