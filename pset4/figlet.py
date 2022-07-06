# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
import sys
from pyfiglet import Figlet
import random

# Verifica as condicoes, se o usuario nao fornecer nenhuma fonte, definir fonte como aleatoria
if len(sys.argv) == 1:
    randomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font  "):
    randomFont = False
else:
    sys.exit("Invalid usage")

figlet = Figlet()

# Traz as fontes para o arquivo
figlet.getFonts()

if randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    font = random.choice(figlet.getFonts())

# Pede para o usuario um texto e imprime o texto formatado.
text = input("Input: ")
print("Output:")
print(figlet.renderText(text))
# 05/07
