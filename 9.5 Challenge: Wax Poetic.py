import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuosly"]

noun1 = ""
noun2 = ""
noun3 = ""
verb1 = ""
verb2 = ""
verb3 = ""
adjective1 = ""
adjective2 = ""
adjective3 = ""
preposition1 = ""
preposition2 = ""
preposition3 = ""
adverb1 = ""
adverb2 = ""
adverb3 = ""
num = 0


while num < 3:
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)

    while noun2 == noun1:
        noun2 = random.choice(nouns)

    while noun3 == noun1 or noun3 == noun2:
        noun3 = random.choice(nouns)

    num += 1

num = 0
while num < 3:
    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)

    while verb2 == verb1:
        verb2 = random.choice(verbs)

    while verb3 == verb1 or verb3 == verb2:
        verb3 = random.choice(verbs)

    num += 1

num = 0
while num < 3:
    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    adjective3 = random.choice(adjectives)

    while adjective2 == adjective1:
        adjective2 = random.choice(adjectives)

    while adjective3 == adjective1 or adjective3 == adjective2:
        adjective3 = random.choice(adjectives)

    num += 1

num = 0
while num < 3:
    preposition1 = random.choice(prepositions)
    preposition2 = random.choice(prepositions)
    preposition3 = random.choice(prepositions)

    while preposition2 == preposition1:
        preposition2 = random.choice(prepositions)

    while preposition3 == preposition1 or preposition3 == preposition2:
        preposition3 = random.choice(prepositions)

    num += 1

num = 0
while num < 3:
    adverb1 = random.choice(adverbs)
    adverb2 = random.choice(adverbs)
    adverb3 = random.choice(adverbs)

    while adverb2 == adverb1:
        adverb2 = random.choice(adverbs)

    while adverb3 == adverb1 or adverb3 == adverb2:
        adverb3 = random.choice(adverbs)

    num += 1

print(f"{adjective1} {noun1}")
print( )
print(f"{adjective1} {noun1} {verb1} {preposition1} the {adjective2} {noun2} {adverb1}, the {noun1} {verb2}")
print(f"the {noun2} {verb3} {preposition2} a {adjective3} {noun3}")

