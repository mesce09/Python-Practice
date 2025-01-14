import random
MAX_LINES=3
MAX_BET=10000000000
MIN_BET=1
ROWS=3
COLS=3
#symbolcount is the count of each symbol which can be selected in each row
Symbolcount={
    "!":6,
    "@":5,
    "#":4,
    "$":3
}
#symbolvalues is the multiplier value for each symbol
Symbolvalues={
    "!":1.5,
    "@":2,
    "#":3,
    "$":5
}

#function to create the slot machine slots
def slotspin(rows,cols,symbols):
    all_symbols=[]
    for symbols,Symbolcount in symbols.items():
        for _ in range(Symbolcount):
            all_symbols.append(symbols)

    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

#function to print slots
def printslot(columns):
    for row in range(len(columns[0])):
        for i,colum in enumerate(columns):
            if i != len(columns) - 1:
                print(colum[row],end=" | ")
            else:
                print(colum[row],end="")
        print()

#function to make deposit
def get_deposit():
    while True:
        amount=input("How much you want to deposit? \n$")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("invalid amount")
        else:
            print("invalid value")
        
    return amount 

#function to get line user want to bet on starting from line 1
def get_lines():
    while True:
        lines=input("enter the number of lines you want to bet on \nSelect a value between 1 - " +str(MAX_LINES)+" ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("invalid Lines entered")
        else:
            print("invalid value")                 
    return lines

#function to get a bet
def get_bets():
    while True:
        betamount=input("How much you want to bet on each line? \n$")
        if betamount.isdigit():
            betamount=int(betamount)
            if MIN_BET<=betamount<=MAX_BET:
                break
            else:
                print("invalid amount")
        else:
            print("invalid value")
    return betamount

#function to check the winnings of the player
def checkwin(columns,lines,bet, values):
    winnings=0
    winningline=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symboltocheck=column[line]
            if symbol!=symboltocheck:
                break
        else:
            winnings+=values[symbol]*bet
            winningline.append(line+1)
    return winnings, winningline   

#function for the game            
def spin(balance):
    lines=get_lines()
    while True:
        bet=get_bets()
        totalbet=bet*lines
        if totalbet>balance:
            print(f"Insufficient funds, select a bet less than ${balance/lines}")
        else:
            print(f"You are betting ${totalbet} on {lines} lines")
            break
    slots=slotspin(ROWS,COLS,Symbolcount)
    printslot(slots)
    winnings,winninglines=checkwin(slots,lines,bet,Symbolvalues)
    print(f"You won ${winnings}.")
    print(f"you won in line: ",*winninglines )
    return winnings-totalbet
               
def main():
    balance=get_deposit()
    while True:
        print(f"Your current balance is ${balance}")
        ans=input("press enter to play(q to quit). ")
        if ans=="q":
            break
        balance+=spin(balance)
    print(f"current balance{balance}")
main()
