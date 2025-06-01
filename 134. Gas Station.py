# O(n power 2)


def canCompleteCircuit(self, gas, cost):
    differ = []

    for i in range(len(gas)):
        differ.append(gas[i] - cost[i])

    total = sum(differ)
    if total < 0:
        return -1

    for i in range(len(differ)):
        if differ[i] >= 0:
            result = 0
            success = True

            for j in range(len(gas)):
                idx = (i+j) % len(gas)
                result = (result + gas[idx]) - cost[idx]
                if result < 0:
                    success = False
                    break

            if success:
                return i

    return -1


#  O(n)

def canCompleteCircuit3(self, gas, cost):
    total = 0
    currunt = 0
    start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        currunt += diff
        if currunt < 0:
            start = i+1
            currunt = 0

    return start if total >= 0 else -1

