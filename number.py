import random

def getSetOfNumber():
    result = []
    count = 6
    A = list(range(38))
    while count != 0:
        temp = random.sample(A,1)
        value = temp[0]
        result.append(value + 1)
        A.remove(value)
        count = count - 1
    result.append(random.randint(1,8))
    return result

if __name__ == "__main__":
    count = 10
    while count != 0:
        print(getSetOfNumber())
        count = count - 1