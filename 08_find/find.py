text = "X-DSPAM-Confidence:    0.8475";
position = text.rfind(' ')+1

desiredNumber = float(text[position:])

print(desiredNumber)
