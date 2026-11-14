def simple_intrest(principal, intrest, time):
    return (principal * intrest * time) / 100

if __name__ == "_main_":
    p = int(input("Enter principal amount: "))
    i = float(input("Enter interest rate: "))
    t = int(input("Enter time in years: "))

    print("Simple interest is:", simple_intrest(p, i, t))