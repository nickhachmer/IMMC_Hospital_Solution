import math


def sigmoid(z):
    s = []
    denom = 0
    for i in range(len(z)):
        denom += math.e ** z[i]

    for i in range(len(z)):
        s.append(math.e**z[i] / denom)

    return s

print(sigmoid([1,2,3,4,1,2,3]))
