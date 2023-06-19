cats = []

i = 0
while i < 100:
    cats.append("no_hat")
    i += 1


print(cats)

n = 0
# round 1
while n < 100:
    a = 0
    while a < 100:
        if cats[a] == "no_hat":
            cats[a] = "hat"
        else:
            cats[a] = "no_hat"
        a += 1
    n += 1
    print(cats)

    # round 2
    b = 1
    while b < 100:
        if cats[b] == "no_hat":
            cats[b] = "hat"
        else:
            cats[b] = "no_hat"
        b += 2
    n += 1
    print(cats)

    # round 3
    c = 2
    while c < 100:
        if cats[c] == "no_hat":
            cats[c] = "hat"
        else:
            cats[c] = "no_hat"
        c += 3
    n += 1
print(cats)
print(n)