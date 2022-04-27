# implement a program that prompts the user for a str of text and then outputs that same text but
# with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
# 20.04

txt = str(input("Input: "))

txt = txt.replace("a", "")
txt = txt.replace("A", "")
txt = txt.replace("e", "")
txt = txt.replace("E", "")
txt = txt.replace("i", "")
txt = txt.replace("I", "")
txt = txt.replace("o", "")
txt = txt.replace("O", "")
txt = txt.replace("u", "")
txt = txt.replace("U", "")

print("Output: " + txt)
