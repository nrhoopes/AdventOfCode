# Nick Hoopes
# Advent of Code 2023 Day 1 Part 2 solution
class calibrationDecipher:
    def __init__(self) -> None:
        self.inputStream = open("Day1.txt")
        self.eachCalibration = []
        self.spelledNumbers = {
            "one" : "1",
            "two" : "2",
            "three" : "3",
            "four" : "4",
            "five" : "5",
            "six" : "6",
            "seven" : "7",
            "eight" : "8",
            "nine" : "9"
        }
        self.sum = 0

        # Loop through each line of the file
        for i in self.inputStream:
            self.eachCalibration.append(self.extractNumber(i))

        # Once everything is sanitized, add up all numbers
        for i in self.eachCalibration:
            self.sum += i

    # Public method replaceSpelled
    # Arguments:
    #   - str: The str to search through to find spelled out numbers and replace them
    #
    # Uses dict 'self.spelledNumbers'
    #
    # This method will accept a string and will search through it character by character
    # to find any instances of spelled out numbers, and will replace them with their respective
    # digit.  It will also tag on the last letter of that number for the sake of special
    # cases such as 'twone'.
    #
    # Ex:
    #   self.replaceSpelled('sixfourgkdlxtqmbzkgmpmcsevenhzrt4')
    # Returns:
    #   '6x4rgkdlxtqmbzkgmpmc7nhzrt4'
    #
    def replaceSpelled(self, str):
        newStr = ""
        for i in str:
            newStr += i
            for word, number in self.spelledNumbers.items():
                temp = newStr.replace(word, number)
                # Required to handle 'twone'
                if temp != newStr:
                    newStr = temp
                    newStr += i
                else:
                    newStr = temp
            print(newStr)
        return newStr

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
        str = self.replaceSpelled(str)
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
# Answer to part 2: 53894
MagicCalibrationMachine = calibrationDecipher()
print(MagicCalibrationMachine.sum)
