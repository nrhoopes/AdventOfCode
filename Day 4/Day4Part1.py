class lotteryScratcher:
    def __init__(self) -> None:
        self.inputStream = open('Day4.txt')
        self.splitCardList = []
        self.cardValueTotal = 0

        for line in self.inputStream:
            self.splitCardList.append(self.splitCard(line))

        for card in self.splitCardList:
            self.cardValueTotal += self.calculateCardValue(card)
    
        # for i in self.splitCardList:
        #     print(i)

        print("Part 1: " + str(self.cardValueTotal))


    # Public method splitCard
    # Arguments:
    #   - card: A line from a scratchcard containing card number, winnings numbers, and your numbers
    #
    # splitCard will take the passed in 'card' and will split it into a list containing three
    # elements, the first being the card number, the second being a list of integers that are
    # the winning numbers for the card, and the third is also a list of integers that are your
    # numbers for the card.
    #
    # Ex:
    #   self.splitCard('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
    # Returns:
    #   ['Card 1', [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]]
    def splitCard(self, card):
        temp = card.split(':')
        for i in temp[1].split('|'):
            temp.append(i)
        del temp[1]

        # List comprehension is pretty cool!
        temp[1] = temp[1].split(' ')
        temp[1] = [int(x) for x in temp[1] if x]
        temp[2] = temp[2].split(' ')
        temp[2] = [int(x) for x in temp[2] if x]
        
        return temp
    
    # Public method calculateCardValue
    # Arguments:
    #   - card: a card that has been split into the format defined by self.splitCard()
    #
    # calculateCardValue will calculate the score of an individual card and will return
    # it as an integer.  It does this by looping through each of the played numbers and
    # checking if they exist in the winning numbers list. Card values are calculated as such:
    #       1 for the first match, then doubled for each match after the first
    #
    # Ex:
    #   self.calculateCardValue(['Card 1', [41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]])
    # Returns:
    #   8
    def calculateCardValue(self, card):
        cardValue = 0
        for myNumber in card[2]:
            if myNumber in card[1]:
                # print(str(myNumber) + " is a winning number in " + card[0])
                if cardValue == 0:
                    cardValue = 1
                else:
                    cardValue *= 2
        return cardValue
    
lotteryScratcher()