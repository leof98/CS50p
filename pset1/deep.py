# Implement a program that prompts the user for the answer to
# the Great Question outputting Yes if the user inputs 42 
# or (case-insensitively) forty-two or forty two.
# Otherwise output No.

resp = str(input("What's the answer to the Great Question of Life, the Universe and Everything? "))
if resp.strip() == "42" or resp.lower() == "forty two" or resp.lower() == "forty-two":
    print("Yes")
else:
    print("No")
    
# 13.04
