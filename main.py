import numpy as np
import matplotlib.pyplot as plt


def create_odometry_map(file):
    """
        Creates a map based on file input.
        :param file: file that function reads
        :return: map
    """
    encoderL = []
    encoderR = []
    time = []

    global robotLength
    robotLength = 0.1

    with open(file) as f:
        content = f.readlines()

    for line in content:
        lineCut = line.split(" ")
        encoderL.append(float(lineCut[0]))
        encoderR.append(float(lineCut[1]))
        time.append(float(lineCut[2]) / 10 ** 9)
        time_diff = np.diff(time)

    def odometry(x, y, date, theta, left, right):
        d = (left + right) / 2
        fi = (right - left) / (2 * robotLength)
        x1 = x + (date * d * np.cos(theta))
        y1 = y + (date * d * np.sin(theta))

        theta1 = theta + fi * date

        return x1, y1, theta1

    def createMap():
        x = [0]
        y = [0]
        theta = [0]

        for i in range(len(encoderL) - 1):
            x1, y1, theta1 = odometry(x[i], y[i], time_diff[i], theta[i], encoderL[i], encoderR[i])
            x.append(x1)
            y.append(y1)
            theta.append(theta1)

        plt.plot(x, y)
        plt.show()

    createMap()

create_odometry_map('Test.txt')
