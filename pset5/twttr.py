def main():
    txt = input("Input: ")
    # Chama a funcao para retirar as vogais
    new_txt = shorten(txt)
    # Imprime o texto
    print("Output: " + new_txt)

def shorten(word):
    new_text = ""
    # Loop por cada letra
    for letter in word:
    # Se a letra nao estiver na lista, adiciona ela
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            new_text += letter
    # retorna o texto sem as vogais
    return new_text

if __name__ == "__main__":
    main()
# 12/07
