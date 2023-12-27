class almanacDecipher:
    def __init__(self) -> None:
        self.inputStream = open("Day5.txt")
        self.lines = []
        self.seeds = []
        self.maps = []
        self.mapTitles = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']

        for i in self.inputStream:
            if i == "\n":
                pass
            else:
                self.lines.append(i.strip('\n'))

        for i in self.lines[0].split():
            if i == 'seeds:':
                pass
            else:
                self.seeds.append(int(i))

        print(self.seeds)

        self.maps = self.generateMaps(self.lines[1:])

    def generateMaps(self, unsortedMaps):
        sortedMaps = []
        for i in unsortedMaps:
            temp = []
            if i in self.mapTitles:
                pass

almanacDecipher()