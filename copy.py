import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuosly"]

noun1 = ""
noun2 = ""
noun3 = ""
num_nouns = 0

while num_nouns < 3:
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)

    while noun2 == noun1:
        noun2 = random.choice(nouns)

    while noun3 == noun1 or noun3 == noun2:
        noun3 = random.choice(nouns)

    num_nouns += 1

print(noun1)
print(noun2)
print(noun3)