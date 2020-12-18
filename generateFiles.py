from random import randint, choice, shuffle
 
class BeeNameGenerator(object):
    VOWELS = (
        (('start', 'middle', 'end'), (
                (5, ("a", "e", "i", "o", "u")),
                (1, ("ae", "ai", "ao", "au", "aa", "ea", "eo", "eu", "ee", "ia",
                     "io", "iu", "ii", "oa", "oe", "oi", "ou", "oo", "eau", "y"))
        )),
        (('middle'), (
            (1, ("'",)),
        ))
    )
    CONSONANTS = (
        (('start', 'middle', 'end'), (
                (3, ("a", "b", "c", "d", "f", "g", "h", "j", "l", "m", "n", "p",
                     "r", "s", "t", "v")),
                (1, ("x", "y", "z", "sc", "ch", "gh", "ph", "sh", "th", "sk", "wk", "st"))
        )),
        (('middle', 'end'), (
                (1, ("ck", "eal", "us", "ss")),
        )),
        (('start', 'middle'), ((2, ("br", "dr", "fr", "gr", "ab", "bz")),
                (1, ("cr", "pr", "sr", "tr", "qu", "wh", "cl", "fl", "gl", "kl",
                     "ll", "pl", "sl", "str"))
        )),
    )
    SYLLABLES_POOL = [[], []]
    for i, group in enumerate((VOWELS, CONSONANTS)):
        pool = SYLLABLES_POOL[i]
        for place, pack in group:
            for frequency, letters in pack:
                for letter in letters:
                    pool.extend(((letter, set(place)),) * frequency)
  
    def get_new_name(self):
        return self.generate_name(self.min_syllable, self.max_syllable)
 
    @classmethod
    def generate_name(cls, min_syllable, max_syllable, base=""):
        length, pool = randint(min_syllable, max_syllable), randint(0, 1)
        for i in range(1, length + 1):
            while True:
                letter, place = choice(cls.SYLLABLES_POOL[pool])
                if i == 1:
                    if 'start' not in place:
                        continue
                elif i == length:
                    if 'end' not in place:
                        continue
                else:
                    if 'middle' not in place:
                        continue
                base += letter
                pool = abs(pool - 1)
                break
        return base.title()


hFull = open("fileFull.txt", "w")
hNumber = open("fileNumbers.txt", "w")
declare = []
names = []
numbers = []
mapping = dict()

while len(mapping) < 5001:
    name = BeeNameGenerator.generate_name(min_syllable=3, max_syllable=7)
    number = randint(1000000000, 9999999999)
    if name not in names and number not in numbers:
        numbers.append(number)
        names.append(name)
        hFull.write(str(number) + ':' + name + '\n')
        mapping[number] = name

hFull.close()
keys = list(mapping.keys())
shuffle(keys)

for key in keys[1:]:
    hNumber.write(str(key) + '\n')

hNumber.close()

print(mapping[keys[0]])
print(keys[0])
