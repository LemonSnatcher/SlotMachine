
MAX_LINES = 3


#Continually asks user to give us a valid amount until we get a proper amount
def deposit():
    while True:
        funds = input("Deposit Amount? $")
        if funds.isdigit():
            funds = int(funds)
            if funds > 0:
                break
            else:
                print("Must be greater than 0.")
        else:
            print("Please enter a valid whole number.")

    return funds

#Same as deposit but for lines were betting on
def get_number_of_lines():
    while True:
        lines = input("How many lines are you betting (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Must be a valid number of lines.")
        else:
            print("Please enter a valid whole number.")
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()
