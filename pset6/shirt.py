import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    first_file = splitext(sys.argv[1])
    second_file = splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif check_file(first_file) == False:
        sys.exit('Invalid input')
    elif check_file(second_file) == False:
        sys.exit('Invalid input')
    elif check_both(first_file, second_file) == False:
        sys.exit('Input and output have different extensions')

    # Verifica se o arquivo passado como argumento existe
    # Realiza as funcoes de imagem importadas
    try:
        image_input = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')
    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(image_input, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])

# Funcao que verifica a extensao dos arquivos
def check_file(file):
    if file[1] in ['.png', '.jpg', '.jpeg']:
        return True
    return False

# Funcao que verifica se a extensao e igual em ambos arquivos
def check_both(file1, file2):
    if file1[1] == file2[1]:
        return True
    return False

if __name__ == '__main__':
    main()
# 17.07
