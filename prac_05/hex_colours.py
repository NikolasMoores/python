COLOUR_DICTIONARY = {"AliceBlue": "#f0f8ff", "black": "#000000", "brown": "	#a52a2a", "chocolate": "#d2691e", "coral": "#ff7f50",
                     "CornflowerBlue": "#6495ed", "DarkKhaki": "#bdb76b", "aquamarine2": "#76eec6", "linen": "#faf0e6", "plum": "#dda0dd"}


colour_code = input("Enter colour: ")

while colour_code != "":
    if colour_code in COLOUR_DICTIONARY:
        print(COLOUR_DICTIONARY[colour_code])
    else:
        print("Invalid colour")
    colour_code = input("Enter colour: ")
