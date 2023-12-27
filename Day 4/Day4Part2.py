class lotteryScratcher:
    def __init__(self) -> None:
        self.inputStream = open('Day4.txt')
        self.splitCardList = []

        for line in self.inputStream:
            self.splitCardList.append(self.splitCard(line))

        for card in self.splitCardList:
            self.calculateCardValue(card)
    
        # I'd advise against uncommenting this with large datasets
        # for i in self.splitCardList:
        #     print(i)

        print("Part 2: " + str(len(self.splitCardList)))


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
    # calculateCardValue has been updated to now calulate how many copies of tickets
    # you earn one the passed in 'card' and will add them to the list self.splitCardList
    # to be evaluated again. And boy does it take a while to do that.
    def calculateCardValue(self, card):
        currentCardNum = int(card[0][4:])
        cardsToCopy = 0
        for myNumber in card[2]:
            if myNumber in card[1]:
                cardsToCopy += 1
        
        for i in range(cardsToCopy):
            self.splitCardList.append(self.splitCardList[currentCardNum + i])
    
lotteryScratcher()