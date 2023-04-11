n = 1.233534
print(f"The value of 'n' is {n:.2f}")

n = 11233534
print(f"The value of 'n' is {n:,}")

n = 11233534
print(f"The value of 'n' is {n:,.2f}")

balance = 2000
spent = 256.35
balance = balance - spent
print(f"After spending ${spent:.2f}, I was left with ${balance:,.2f}")

ratio = 0.9
print(f"Over {ratio:.2%} of Pythonistas sat 'Real Python rocks!'")