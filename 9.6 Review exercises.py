# 1
captains = {}

# 2
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"

# 3
if "Enterprise" not in captains:
    captains["Enterprise"] = "unknown"

if "Discovery" not in captains:
    captains["Discovery"] = "unknown"

# 4
for ship, captain in captains.items():
    print(f"The {ship} is captained by {captain}")

# 5
del captains["Discovery"]

print(captains)

captains = dict(
    [
        ("Enterprise", "Picard"),
        ("Voyager", "Janeway"),
        ("Defiant", "Sisko"),
    ]
)
