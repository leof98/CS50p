# Implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the 
# latter might be any values in the list. Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user 
# again. Assume that every month has no more than 31 days.

def main():
    list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        date = input("Date: ")
        try:
            # Separa a variavel em uma lista com /
            month, day, year = date.split("/")
            month = month.replace(" ","")
            year = year.replace(" ","")
            # Verifica as condicoes
            if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                break
        except:
            try:
                # Separa a variavel em uma lista com espacos
                old_month, old_day, year = date.split(" ")
                if not old_day.endswith(","):
                    main()
                # Faz um loop para encontrar o numero do mes
                for i in range(len(list)):
                    if old_month == list[i]:
                        month = i + 1
                day = old_day.replace(",","")
                # Verifica as condicoes
                if (int(month) >= 1 and int(month) <= 12) and (int(day) >= 1 and int(day) <= 31):
                    break
            except:
                print()
                pass

    # Imprime a data formatada
    print(f"{year}-{int(month):02}-{int(day):02}")
main()
