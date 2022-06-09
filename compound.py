def compound_interest(p, c, r, n, t, itr):
    if itr == n * t:
        return (c - p)
    interest = c* (r / (n * 100))
    return compound_interest(p, c+ interest, r, n, t, itr + 1)

p = float(input("Enter the principal amount = "))
r = float(input("Enter the interest rate :"))  
n = int(input("Enter compound frequency / year = "))
t = int(input("Enter no.of years:"))
        
ci = compound_interest(p, p, r, n, t, 0)
print("Compound interest = ",round(ci, 2))
