def computepay(h,r):
    if h>40:
        rate = (r*1.5)*(h-40)
    return ((h-5)*r)+rate
hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print ("Pay",p)

