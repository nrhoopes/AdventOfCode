class camelMaps:
    def __init__(self) -> None:
        self.inputStream = open("Day8.txt")
        self.directions = ''
        self.maps = {}
        self.position = 'AAA'
        self.steps = 0

        for i, val in enumerate(self.inputStream):
            if i == 0:
                self.directions = val.strip('\n')
            elif i == 1:
                continue
            else:
                self.maps[val.split('=')[0].strip(' ')] = self.createTuple(val.split('=')[1].strip('\n').lstrip(' '))
        
        print("Part 1: " + str(self.followSteps(0)))

    def followSteps(self, stepped):
        steps = stepped
        for i in self.directions:
            if self.position == 'ZZZ':
                return steps
            possibleRoutes = self.maps.get(self.position)
            if i == 'R':
                self.position = possibleRoutes[1]
                steps += 1
            elif i == 'L':
                self.position = possibleRoutes[0]
                steps += 1
            else:
                print("Data is incorrect or corrupted.")
                quit()
        
        if self.position == 'ZZZ':
            return steps
        else:
            return self.followSteps(steps)


    def createTuple(self, str):
        str = tuple(str.strip('(').strip(')').split(', '))
        return str

camelMaps()