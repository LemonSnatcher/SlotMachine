import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

sym_count = {
    "A" : 2,
    "B" : 3,
    "C" : 4,
    "D" : 6,
}
#How we randomize the symbols in play
def get_spin(row, cols, syms):
    all_syms = []
    for syms, sym_count in syms.items():
        for _ in range(sym_count):
            all_syms.append(syms)
    #Symbols wont appear more than their sym count Ex. A can't appear more than 2 times
    columns = []
    for _ in range(cols):
        column = []
        curr_syms = all_syms[:]
        for _ in range(row):
            val = random.choice(curr_syms)
            curr_syms.remove(val)
            column.append(val)
        
        columns.append(column)
    return columns

def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])


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

#Rudamentary System asking if your ready to spin
def slot_pull():
    while True:
        pull = input("Ready to spin? Yes or No?")
        if pull.isdigit(): #Currently only rejects numbers but will let any string through
            print("Yes or No?")
        else:
            break

def main():
    balance = deposit()
    lines = get_number_of_lines()
    #Makes sure you have enough balance for the wager
    while True:
        wager = get_bet()
        total_wager = wager * lines
        if total_wager > balance:
            print(f"Not enough cash for that i'm afraid, you only have ${balance} ")
        else:
            break
    
    
    print(f"Current Wager is ${wager} on {lines} lines. Total wager is: ${total_wager}")
    slots = get_spin(ROWS, COLS, sym_count)
    slot_pull()
    print_slots(slots)

main()
