hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the Rate:")
r = float(rate)
if h <= 40:
    print(h * r)
elif h > 40:
    pay = (40 * r + (h - 40) * (1.5 * r))
print("Pay:", pay)
