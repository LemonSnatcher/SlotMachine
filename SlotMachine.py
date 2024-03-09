
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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
                print("Only 1 to 3 lines a wager.")
        else:
            print("Please enter a valid number of lines.")
    return lines

#Same as the previous ask for proper wager and wont break until condition is met
def get_bet():
    while True:
        wager = input("What's your wager per line? $")
        if wager.isdigit():
            wager = int(wager)
            if MIN_BET <= wager <= MAX_BET:
                break
            else:
                print(f"Wagers run from ${MIN_BET} to ${MAX_BET}.")
        else:
            print("Please enter a proper wager.")

    return wager

def main():
    balance = deposit()
    lines = get_number_of_lines()
    wager = get_bet()
    total_wager = wager * lines
    print(f"Current Wager is ${wager} on {lines} lines. Total wager is: ${total_wager}")

    print(balance, lines)

main()
