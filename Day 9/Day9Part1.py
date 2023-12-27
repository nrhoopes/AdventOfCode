# Oasis and sand instability sensor
class oasisSensor:
    def __init__(self) -> None:
        self.inputStream = open("Day9.txt")       # Read in values from input
        self.currentPredict = []                  # The current line's set from the input
        self.extrapolatedSum = 0                  # The sum of each extrapolated value at the top of each set

        for line in self.inputStream:
            self.currentPredict.append(list(map(int, line.split()))) # Start by splitting the line into a list of numbers
            currentList = self.currentPredict[len(self.currentPredict) - 1]
            # Hey that all() function is pretty cool, didn't know about that before
            while not all(x == 0 for x in currentList): # Work way down the list until you reach all 0's
                tempList = []
                for i in range(len(currentList) - 1):
                    tempList.append(currentList[i + 1] - currentList[i])
                self.currentPredict.append(tempList)
                currentList = self.currentPredict[len(self.currentPredict) - 1]

            # Add new zero to the bottom of the list
            self.currentPredict[len(self.currentPredict) - 1].append(0)
            # print(self.currentPredict)

            # Work way back up and extrapolate
            for i in range(len(self.currentPredict) - 2, -1, -1):
                thisList = self.currentPredict[i] # Start at the second to last list (to avoid off by 1)
                lastList = self.currentPredict[i + 1]

                extrapolatedValue = thisList[len(thisList) - 1] + lastList[len(lastList) - 1]
                self.currentPredict[i].append(extrapolatedValue)
            
            # print(self.currentPredict)
            # Once you've made your way to the top, add the final extrapolated value to the sum.
            self.extrapolatedSum += self.currentPredict[0][len(self.currentPredict[0]) - 1]
            self.currentPredict = [] # Reset currentPredict to start over
        print(self.extrapolatedSum)

# Answer to Part 1: 1974913025

oasisSensor()
