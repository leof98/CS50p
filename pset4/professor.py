# Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits.
# No need to support operations other than addition (+). Prompts the user to solve each of those problem.
# If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
# allowing the user up to three tries in total. If the user has still not answered correctly after three tries,
# The program should output the correct answer.  The program should ultimately output the user’s score, a number out of 10.
import random


def main():
    level = get_level()
    score = generate_game(level)
    print("Score:", score)

# Loop infinito que pede um numero de 1 a 3 e rejeita o resto
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

# Retorna 2 numeros aleatorios dependendo do argumento
def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

# 3 tentativas ao usuario para acertar o problema, se acertar retorna verdadeiro
# Do contrario, retorna falso e imprime o resultado correto
def generate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            question = int(input(f"{x} + {y} = "))
            if question == (x + y):
                return True
            else:
                print("EEE")
                count_tries += 1
        except:
            print("EEE")
            count_tries += 1
            pass
    print(f"{x} + {y} = {x + y}")
    return False


def generate_game(level):
    count_round = 0
    score = 0
    while count_round < 10:
        x, y = generate_integer(level)
        response = generate_round(x, y)
        if response == True:
            score += 1
        count_round += 1
    return score


if __name__ == "__main__":
    main()
