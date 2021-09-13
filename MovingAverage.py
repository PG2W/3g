import random
import unittest


class MovingAverage:
    def __init__(self, n):
        self.n = n
        self.samples = []

    def addSample(self, value):
        if len(self.samples) > self.n - 1:
            del self.samples[0]
            self.samples.append(float(value))
        else:
            self.samples.append(float(value))

    def getAverage(self):
        return sum(self.samples) / len(self.samples)

    def showSamples(self):
        print("Current samples: ", self.samples)


class TestMovingAverage(unittest.TestCase):
    def setUp(self):
        ma = MovingAverage(10)

    def test_addSample(self):



ma = MovingAverage()

for x in range(0, 1000):
    ma.addSample(random.randrange(1, 56))
    print(ma.getAverage())
