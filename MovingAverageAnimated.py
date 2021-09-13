import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
import threading
import unittest
matplotlib.use("TkAgg")



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
        if len(self.samples) == 0:
            return 0
        return sum(self.samples) / len(self.samples)


fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
#ax2 = fig.add_subplot(1, 1, 1)
xs = []
ys = []
inputlist = []
lastaverage = float
currentaverage = float


def animate(i, xs, ys):
    global lastaverage
    global currentaverage
    global inputlist
    currentaverage = ma.getAverage()
    if currentaverage != lastaverage:
        xs.append(ma.getAverage())
        ys.append(dt.datetime.now().strftime('%H:%M:%S'))
        if len(ma.samples) == 0:
            inputlist.append(0)
        else:
            inputlist.append(ma.samples[-1])
        lastaverage = currentaverage

    xs = xs[-20:]
    ys = ys[-20:]
    inputlist = inputlist[-20:]

    ax1.clear()
    ax1.plot(ys, xs, ys, inputlist, '--')
#    ax2.plot(inputlist, xs, 'o')

    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Moving average over time')
    plt.ylabel('Moving Average')


def keepAsking():
    while True:
        ma.addSample(float(input("Add a sample: ")))


ma = MovingAverage(int(input("How many samples to calculate moving average over?: ")))
t2 = threading.Thread(target=keepAsking)
t2.start()
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=500)
plt.show()




