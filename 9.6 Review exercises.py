# 1
captains = {}

# 2
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# 3
if "Enterprise" in captains:
    print("ok")
else:
    captains["Enterprise"] = "unknown"

if "Discovery" in captains:
    print("ok")
else:
    captains["Discovery"] = "unknown"

# 4
for captain in captains:
    print(f"The {captain} is captained by {captains[captain]}")

# 5
del captains["Discovery"]

print(captains)

dict(captains)
