# 1
word1 = "Animals"
word2 = "Badger"
word3 = "Honey Bee"
word4 = "Honeybadger"
print(word1.lower())
print(word2.lower())
print(word3.lower())
print(word4.lower())

# 2
print(word1.upper())
print(word2.upper())
print(word3.upper())
print(word4.upper())

# 3
string1 = "     Filet Mignon"
string2 = "Brisket     "
string3 = "  Cheeseburger   "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

# 4
string4 = "Becomes"
string5 = "becomes"
string6 = "BEAR"
string7 = "   bEautiful"
print(string4.startswith("be"))
print(string5.startswith("be"))
print(string6.startswith("be"))
print(string7.startswith("be"))

#5
string4 = string4.lower()
string5 = string5.lower()
string6 = string6.lower()
string7 = string7.lower().lstrip()
print(string4.startswith("be"))
print(string5.startswith("be"))
print(string6.startswith("be"))
print(string7.startswith("be"))