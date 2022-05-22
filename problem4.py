score = float(input("Enter Score: "))
if (score > 1.0 or score < 0.0):
    print("out of range")
elif score >= 0.9:
    print("A Grade")
elif score >= 0.8:
    print("B Grade")
elif score >= 0.7:
    print("C Grade")
elif score >= 0.6:
    print("D Grade")
elif score < 0.6:
    print("F Grade")
