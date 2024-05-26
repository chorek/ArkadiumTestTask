

class Table:
    def __init__(self, wait):
        self.dictionary = ''

    def load(self):
        self.dictionary = {
            "Pungent condiment (7)": 'mustard',
            "Glaswegians, Aberdonians, etc (5)": 'scots',
            "Speedy (5)": 'swift',
            "Lower back pain (7)": 'lumbago',
            "Unlawful (7)": 'illicit',
            "Approximately (5)": 'about',
            "Domesticated polecat (6)": 'ferret',
            "Stock of wines (6)": 'cellar',
            "Towards the stern of a ship (5)": 'abaft',
            "Boasted (7)": 'bragged',
            "Pariah (7)": 'outcast',
            "Two times (5)": 'twice',
            "Lone Star state (5)": 'texas',
            "Aridity (7)": 'dryness',
            "Thick-set powerful breed of dog (7)": 'mastiff',
            "Expertise (5)": 'skill',
            "Recital (anag) (7)": 'article',
            "Water down (6)": 'dilute',
            "Brazilian dance (5)": 'samba',
            "Enjoying a winning streak (2,1,4)": 'onaroll',
            "Yell (5)": 'shout',
            "Vehicle excise duty (4,3)": 'roadtax',
            "Precisely (7)": 'exactly',
            "Compensation (7)": 'redress',
            "Died down (6)": 'abated',
            "On high (5)": 'aloft',
            "Snares (5)": 'traps',
            "Move effortlessly (5)": 'glide',
        }
        assert self.dictionary, "Answers loading failed! No answers in dictionary."


