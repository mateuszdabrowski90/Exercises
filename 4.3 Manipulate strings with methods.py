word = "Jean-luc Picard"
print(word.lower())
print(word.upper())

# removing whitespace on the right side
word2 = "Jean-luc Picard    "
print(word2.rstrip())

# removing whitespace on the left side
word3 = "      Jean-luc Picard"
print(word3.lstrip())

# removing whitespace on both sides
word4 = "      Jean-luc Picard     "
print(word4.strip())

# determining if a string starts with particular string
starship = "Enterprise"
starship.startswith("en")
starship.endswith("rise")