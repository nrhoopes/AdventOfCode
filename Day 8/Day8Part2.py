import sys

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

        self.allStartPoints = []
        # self.allEndPoints = []
        for key in self.maps:
            if key[2] == 'A':
                self.allStartPoints.append(key)
            # elif key[2] == 'Z':
            #     self.allEndPoints.append(key)

        self.steps += self.followSteps(0, self.allStartPoints)
        
        # print("Part 1: " + str(self.followSteps(0)))
        print("Part 2: " + str(self.steps))

    def followSteps(self, stepped, positions):
        print(positions)
        steps = stepped
        for i, pos in enumerate(positions):
            if pos[2] == 'Z':
                print(pos)
                if i + 1 == len(positions):
                    return steps
                else:
                    continue
            else:
                break
        for direction in self.directions:
            for index, pos in enumerate(positions):
                possibleRoutes = self.maps.get(pos)
                if direction == 'R':
                    positions[index] = possibleRoutes[1]
                elif direction == 'L':
                    positions[index] = possibleRoutes[0]
            steps += 1

        for i, pos in enumerate(positions):
            if pos[2] == 'Z':
                if i + 1 == len(positions):
                    return steps
                else:
                    continue
            else:
                break
        
        return self.followSteps(steps, positions)
        





        


    def createTuple(self, str):
        str = tuple(str.strip('(').strip(')').split(', '))
        return str

camelMaps()