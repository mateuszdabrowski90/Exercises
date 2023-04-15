def invest(amount, rate, years):
    n = 1
    while n <= years:
        amount = amount + amount * rate * 0.01
        print(f"year {n}: ${amount:.2f}")
        n = n + 1

amount = float(input("Enter your initial amount: "))
rate = float(input("Enter your annual rate of return: "))
years = int(input("Enter a number of years: "))

invest(amount, rate, years)