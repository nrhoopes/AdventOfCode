# Nick Hoopes
# Advent of Code 2023 Day 1 Part 1 solution
class calibrationDecipher:
    def __init__(self) -> None:
        self.inputStream = open("Day1.txt")
        self.eachCalibration = []
        self.sum = 0

        for i in self.inputStream:
            self.eachCalibration.append(self.extractNumber(i))

        for i in self.eachCalibration:
            self.sum += i
            
    # Public method extractNumber
    # Arguments:
    #   - str: the str to extract numbers from
    #
    # This method will accept a string and will extract the first digit
    # and last digit from the string, append them into a double digit number,
    # and then will cast it to an integer and return it.
    #
    # Ex:
    #   self.extractNumber('5hdusevenooasd6')
    # Returns:
    #   56
    def extractNumber(self, str):
        finDblDigit = ""
        secondDigit = ""
        for i in str:
            if i.isnumeric():
                if len(finDblDigit) < 1:
                    finDblDigit += i
                else:
                    secondDigit = i

        if secondDigit == "":
            finDblDigit += finDblDigit
        else:
            finDblDigit += secondDigit
        if finDblDigit != "":
            return int(finDblDigit)
        else:
            return 0

# Answer to part 1: 53651
MagicCalibrationMachine = calibrationDecipher()
print(MagicCalibrationMachine.sum)
