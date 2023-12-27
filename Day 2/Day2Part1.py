import re

class bagOfCubesGame:
    def __init__(self) -> None:
        self.inputStream = open("Day2.txt")
        self.maxCubes = [12, 13, 14] # RGB
        self.evaluatedGames = []
        self.gameSum = 0

        # For each line in the file
        for i in self.inputStream:
            self.evaluatedGames.append(self.evalMaxCubes(self.splitGame(i)))

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
        
        print(self.gameSum)

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
                
# Part 1 answer: 1931
bagOfCubesGame()