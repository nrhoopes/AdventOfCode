class camelCards:
    def __init__(self) -> None:
        self.inputStream = open("Day7.txt")
        self.powerByHand = {
            "5" : 1,
            "4" : 2,
            "H" : 3,
            "3" : 4,
            "T" : 5,
            "O" : 6,
            "C" : 7
        }
        self.hands = []
        self.evaluatedHands = []

        for line in self.inputStream:
            splitLine = line.split(' ')
            self.hands.append([splitLine[0], 0, splitLine[1].strip('\n')])

        self.evaluateHands(self.hands)
        print(self.rankHands(self.hands))


    def rankHands(self, hands):
        rankedHands = []
        for hand in hands:
            rankedHands.append([hand[0], self.powerByHand.get(hand[1]), hand[2]])
        rankedHands.sort(key=lambda x: x[1], reverse=True)

        posCounter = 1
        powerRating = 0
        for index, hand in enumerate(rankedHands):
            cards = hand[0]
            powerRating = hand[1]


        return rankedHands

    def evaluateHands(self, hands):
        for i, hand in enumerate(hands):
            self.hands[i][1] = self.findHandType(hand[0])

    def findHandType(self, hand):
        sortedCards = self.splitHandByCards(hand)
        fullHouseFirstThree = False
        fullHouseFirstTwo = False
        onePair = False

        for entry in sortedCards:
            if entry[1] == 5:
                return "5"
            elif entry[1] == 4:
                return "4"
            elif entry[1] == 3:
                if fullHouseFirstTwo:
                    return 'H'
                else:
                    fullHouseFirstThree = True
            elif entry[1] == 2:
                if fullHouseFirstThree:
                    return 'H'
                else:
                    fullHouseFirstTwo = True
                
                if onePair:
                    return 'T'
                else:
                    onePair = True
            elif entry[1] == 1:
                continue

        if onePair:
            return "O"
        elif fullHouseFirstThree:
            return "3"
        elif fullHouseFirstTwo:
            return "2"
        else:
            return "C"

        

    def splitHandByCards(self, hand):
        flag = True
        cards = [[hand[0], 1]]
        for card in hand[1:]:
            for index, i in enumerate(cards):
                if card in i:
                    cards[index][1] += 1
                    flag = False
                    break
            if flag:
                cards.append([card, 1])
            else:
                flag = True
        return cards 

camelCards()