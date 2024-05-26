

class Table:
    def __init__(self, wait):
        self.dictionary = ''

    def load(self):
        self.dictionary = {
            "Mix (6)": 'mingle',
            "Aromatic spice (6)": 'nutmeg',
            "Doctors stand-in (5)": 'locum',
            "Waterfall (7)": 'cascade',
            "Popular cheese (7)": 'cheddar',
            "Assumed name (5)": 'alias',
            "Using mocking irony (9)": 'sarcastic',
            "Steadfast in allegiance (5)": 'loyal',
            "Without affectation (7)": 'natural',
            "Affluent (7)": 'wealthy',
            "Brag (5)": 'boast',
            "Dwell (6)": 'reside',
            "Deteriorate (6)": 'worsen',
            "Spite (6)": 'malice',
            "Core (7)": 'nucleus',
            "Medal (anag) (5)": 'lamed',
            "Parvenu (7)": 'upstart',
            "Florida resort (5)": 'miami',
            "Lubricant (6)": 'grease',
            "Without doubt (9)": 'certainly',
            "Akin (7)": 'related',
            "Wheat, barley, oats, etc. (7)": 'cereals',
            "Bloom, blossom (6)": 'flower',
            "Protein present in wheat (6)": 'gluten',
            "Renowned Irish poet (5)": 'yeats',
            "Forbidden (5)": 'taboo'
        }
        assert self.dictionary, "Answers loading failed! No answers in dictionary."

