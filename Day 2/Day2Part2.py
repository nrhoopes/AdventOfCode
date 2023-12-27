import re

class bagOfCubesGame:
    def __init__(self) -> None:
        self.inputStream = open("Day2.txt")
        self.maxCubes = [12, 13, 14] # RGB
        self.evaluatedGames = []
        self.gameSum = 0
        self.powerSum = 0

        # For each line in the file
        for i in self.inputStream:
            self.evaluatedGames.append(self.evalMaxCubes(self.splitGame(i)))
            self.powerSum += self.findPowerOfGame(self.findMaxCubes(self.splitGame(i)))

        # For each game in self.evaluatedGames
        for gameNum, game in enumerate(self.evaluatedGames):
            for i, val in enumerate(game):
                if i == 0:
                    pass
                else:
                    if val and i == len(game) - 1:
                        self.gameSum += (gameNum + 1)
                    elif val:
                        pass
                    else:
                        break

        print("Part 1: " + str(self.gameSum))
        print("Part 2: " + str(self.powerSum))

    # Public method splitGame
    # Arguments:
    #   - str: The string to split
    #
    # Splits a game into it's individual hands and returns a list of each
    def splitGame(self, str):
        return re.split(': |; ', str)
    
    # Public method splitHand
    # Arguments:
    #   - str: The string to split
    #
    # Splits a hand into the number of each color dice and puts them into a list.
    def splitHand(self, str):
        return re.split(', ', str)
    
    # Public method evalMaxCubes
    # Arguments:
    #   - gameList: A list of a game split by each hand (using self.splitGame())
    #
    # evalMaxCubes will enumerate through each entry in the gameList and will
    # return a different list (handPossibility) that contains the game number
    # and then following boolean values corresponding to each hand.  If
    # there are three hands, then there will be three boolean values.  False
    # means that the max was exceeded, True means the hand is valid.
    #
    # Ex:
    #   self.evalMaxCubes(['Game 97', '5 red, 2 green', '8 red', '1 blue, 7 green, 2 red', '7 red, 15 green\n'])
    # Returns:
    #   ['Game 97', True, True, True, True, True, True, True, False]
    def evalMaxCubes(self, gameList):
        handPossibility = []
        for i, j in enumerate(gameList):
            # If the index is 0, then it is the game number
            if i == 0:
                handPossibility.append(j)
            # Otherwise it is a possible hand that needs evaluated
            else:
                hand = self.splitHand(j)
                for i in hand:
                    if 'red' in i:
                        if self.maxCubes[0] >= int(i.split(' ', 1)[0]):
                            handPossibility.append(True)
                        else:
                            handPossibility.append(False)
                    elif 'green' in i:
                        if self.maxCubes[1] >= int(i.split(' ', 1)[0]):
                            handPossibility.append(True)
                        else:
                            handPossibility.append(False)
                    elif 'blue' in i:
                        if self.maxCubes[2] >= int(i.split(' ', 1)[0]):
                            handPossibility.append(True)
                        else:
                            handPossibility.append(False)
        return handPossibility
    
    # Public method findMaxCubes
    # Arguments:
    #   - gameList: A list of a game split by each hand (using self.splitGame())
    #
    # Returns the max number of cubes used in a game, aka the minimum number of
    # cubes required to make the game valid in a list using [Game Name, R, G, B] format.
    #
    # Ex:
    #   self.evalMaxCubes(['Game 97', '5 red, 2 green', '8 red', '1 blue, 7 green, 2 red', '7 red, 15 green\n'])
    # Returns:
    #   ['Game 91', 8, 15, 1]
    def findMaxCubes(self, gameList):
        maxCubesForGame = ['Game 0:', 0, 0, 0]
        for i, j in enumerate(gameList):
            if i == 0:
                maxCubesForGame[0] = j
            else:
                hand = self.splitHand(j)
                for i in hand:
                    if 'red' in i:
                        if maxCubesForGame[1] < int(i.replace(' red', '')):
                            maxCubesForGame[1] = int(i.replace(' red', ''))
                    elif 'green' in i:
                        if maxCubesForGame[2] < int(i.replace(' green', '')):
                            maxCubesForGame[2] = int(i.replace(' green', ''))
                    elif 'blue' in i:
                        if maxCubesForGame[3] < int(i.replace(' blue', '')):
                            maxCubesForGame[3] = int(i.replace(' blue', ''))
        return maxCubesForGame
    
    # Public method findPowerOfGame
    # Arguments:
    #   - maxCubesForGame: A list of the minimum required number of cubes to make a game valid.
    #                      (from self.findMaxCubes)
    #
    # Returns the power of the game which is all of the number of cubes multiplied together.
    def findPowerOfGame(self, maxCubesForGame):
        power = 1
        # Skip the first entry since that is the title of the game.
        for val in maxCubesForGame[1:]:
            power *= val
        return power

                
# Part 1 answer: 1931
# Part 2 answer: 83105
bagOfCubesGame()