class schematicDecoder:
    def __init__(self) -> None:
        self.inputStream = open("Day3.txt")
        self.schematic = []
        self.partNumSum = 0
        self.forbiddenChars = ['.', '\n']

        # Loop through each line of the schematic
        for i in self.inputStream:
            # Verify the endline exists
            if not '\n' in i:
                i = i + '\n'
            self.schematic.append(i)

        # Loop through each part number and add them
        for i in self.findPartNumbers(self.schematic):
            self.partNumSum += int(i)
        
        print(self.findPartNumbers(self.schematic))

        print("Part 1: " + str(self.partNumSum))

    # Public method findPartNumbers
    # Arguments:
    #   - schematic: a list of each line of the schematic
    #
    # findPartNumbers will look through each line of the schematic and will
    # find any numbers that are touching a symbol other than '.' in any direction
    # including diagonally.
    # Ex:
    #   self.findPartNumbers(['467..114..', '...*....21', '..35..633.'])
    # Returns:
    #   ['467', '35']
    def findPartNumbers(self, schematic):
        validPartNumbers = []
        skipLength = False # Set to True to skip the remaining length of a valid number
        for row, line in enumerate(schematic):
            for col, char in enumerate(line):
                if char.isnumeric() and not skipLength:
                    length = self.findLengthOfNum(line, col)
                    # Find any symbols above
                    # verify line exists
                    if row != 0 and not skipLength:
                        lineAbove = schematic[row - 1]
                        # verify bounds exist
                        if col != 0:
                            # go left
                            if not lineAbove[col - 1].isalnum() and lineAbove[col - 1] not in self.forbiddenChars and not skipLength:
                                validPartNumbers.append(line[col:col+length])
                                skipLength = True

                        # middle of line
                        for i in range(length):
                            if not lineAbove[col + i].isalnum() and lineAbove[col + i] not in self.forbiddenChars and not skipLength:
                                validPartNumbers.append(line[col:col+length])
                                skipLength = True

                        if col != len(lineAbove) - 1:
                            # go right
                            if not lineAbove[col + length].isalnum() and lineAbove[col + length] not in self.forbiddenChars and not skipLength:
                                validPartNumbers.append(line[col:col+length])
                                skipLength = True


                    # Find any symbols on same line
                    if col != 0 and not skipLength:
                        if not line[col - 1].isalnum() and line[col - 1] not in self.forbiddenChars and not skipLength:
                            validPartNumbers.append(line[col:col+length])
                            skipLength = True

                    if col != len(line) - 2:
                        if not line[col + length].isalnum() and line[col + length] not in self.forbiddenChars and not skipLength:
                            validPartNumbers.append(line[col:col+length])
                            skipLength = True

                    # Find any symbols below
                    if row != len(schematic) - 1 and not skipLength:
                        lineBelow = schematic[row + 1]
                        # verify bounds exist
                        if col != 0:
                            # go left
                            if not lineBelow[col - 1].isalnum() and lineBelow[col - 1] not in self.forbiddenChars and not skipLength:
                                validPartNumbers.append(line[col:col+length])
                                skipLength = True

                        # middle of line
                        for i in range(length):
                            if not lineBelow[col + i].isalnum() and lineBelow[col + i] not in self.forbiddenChars and not skipLength:
                                validPartNumbers.append(line[col:col+length])
                                skipLength = True
                        
                        if col != len(lineBelow) - 1:
                            # go right
                            if not lineBelow[col + length].isalnum() and lineBelow[col + length] not in self.forbiddenChars and not skipLength:
                                validPartNumbers.append(line[col:col+length])
                                skipLength = True
                elif not char.isnumeric():
                    skipLength = False

        return validPartNumbers

    # Public method findLengthOfNum
    # Arguments:
    #   - line: the full line of the schematic to find the length of a number from
    #   - col: the index that the number to find the length of starts
    #
    # findLengthOfNum accepts a line from the schematic and a column where a number
    # starts, and will find the length of that number on that line.
    #
    # Ex:
    #   self.findLengthOfNum('..23...883..$.', 7)
    # Returns:
    #   3
    def findLengthOfNum(self, line, col):
        i = col
        length = 0
        while line[i].isnumeric():
            length += 1
            i += 1
            if i >= len(line):
                break
        return length

# Part 1: 556057
schematicDecoder()