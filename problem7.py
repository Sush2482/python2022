text = "X-DSPAM-Confidence:    0.8475";
numValue = text.find('0.8475')
numSlice= text[numValue:]
end = float(numSlice)
print(end)
