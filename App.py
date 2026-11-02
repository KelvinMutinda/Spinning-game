import random 
def spin_row():
    symbols=['🌹','🎉','🎂','🤳']

    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print(" | ".join(row))
def get_payout(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🌹':
            return bet *4
        elif row[0]=='🎉':
             return bet *2
        elif row[0]=='🎂':
            return bet * 10
        elif row[0]=='🤳':
            return bet * 5
    return 0

   

def main():
    balance=100
    print('_____Slot Game____')
    print('Symbols: 🌹   🎉  🎂   🤳')

    while balance>0:
        print(f"Current balance : ${balance}")
        bet=input("Place your bet : ")

        if not bet.isdigit():
            print("Enter a valid Number")

        bet=int(bet)

        if bet> balance:
            print("Insufficient funds ")
            continue

        if bet <=0:
            print("Bet must be better than 0")
            continue
        balance-=bet

        row=spin_row()
        print("Spinning \n")
        print_row(row)
        payout=get_payout(row,bet)

        if payout>0:
            print(f"You won ${payout}")
        else:
            print(f"Sorry You lost.Your balance is {balance}")

        balance+=payout


    pass

if __name__=='__main__':
    main()