class boatRace:
    def __init__(self) -> None:
        self.inputStream = open("Day6.txt")
        self.timesForRaces = []
        self.distance = []
        self.totalHoldTimesPerRace = []
        self.part1Ans = 1

        # Split each of the lines into their own lists
        for lineNum, line in enumerate(self.inputStream):
            if lineNum == 0:
                timesTemp = line.split(' ')
                timesTemp = timesTemp[1:]
                self.timesForRaces = [int(x) for x in timesTemp if x]
            elif lineNum == 1:
                distTemp = line.split(' ')
                distTemp = distTemp[1:]
                self.distance = [int(x) for x in distTemp if x]

        for race in range(len(self.timesForRaces)):
            self.totalHoldTimesPerRace.append(self.findBestTimes(self.timesForRaces[race], self.distance[race]))

        for time in self.totalHoldTimesPerRace:
            self.part1Ans *= time

        print("Part 1: " + str(self.part1Ans))

    # Public method findBestTimes
    # Arguments:
    #   - time: the time allocated to the race
    #   - distance: the record distance for that race.
    #
    # findBestTimes will return the total number of possible
    # times that you can hold the button on the boat for to
    # win the race
    def findBestTimes(self, time, distance):
        numOfTimes = 0 # Number of times to hold button and beat distance record
        for startTime in range(time):
            # If (time to hold button) * (remaining time in the race) > distance record
            if ((startTime + 1) * (time - (startTime + 1))) > distance:
                numOfTimes += 1
        return numOfTimes

boatRace()