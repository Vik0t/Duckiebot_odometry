import numpy as np
import matplotlib.pyplot as plt


class Odometry:
    """
        Creates a map based on file input.
    """

    def __init__(self):
        self.file = "Test.txt"  # add your path there
        self.robotLength = 0.1

    def getInfo(self):
        encoderL = []
        encoderR = []
        time = []
        with open(self.file) as f:
            content = f.readlines()
        for line in content:
            lineCut = line.split(" ")
            encoderL.append(float(lineCut[0]))
            encoderR.append(float(lineCut[1]))
            time.append(float(lineCut[2]) / 10 ** 9)
        time_diff = np.diff(time)
        return encoderL, encoderR, time_diff

    def odometry(self, x, y, date, theta, left, right):
        d = (left + right) / 2
        fi = (right - left) / (2 * self.robotLength)
        x1 = x + (date * d * np.cos(theta))
        y1 = y + (date * d * np.sin(theta))

        theta1 = theta + fi * date

        return x1, y1, theta1

    def createMap(self):
        x = [0]
        y = [0]
        theta = [0]
        encoderL, encoderR, time_diff = self.getInfo()

        for i in range(len(encoderL) - 1):
            x1, y1, theta1 = self.odometry(x[i], y[i], time_diff[i], theta[i], encoderL[i], encoderR[i])
            x.append(x1)
            y.append(y1)
            theta.append(theta1)

        plt.plot(x, y)
        plt.show()

output = Odometry()
output.createMap()