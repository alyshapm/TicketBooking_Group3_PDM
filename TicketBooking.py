def menu(stock):
    item_length = 0
    for dest in stock:
        item_length = len(dest) if len(dest) > item_length else item_length
    item_length += 1

    print(f"\n{'Destination':<{item_length}} {'Code':<8} {'Time':<7} {'Price':<10} {'Seats left':<5}")
    print("--------------------------------------------------")

    for name, details in stock.items():
        code, time, qty, price = details
        print(f"{name.capitalize():<{item_length}} {details[code]:<8} {details[time]:<7} Rp.{details[price]:<10} {details[qty]:<5}")

def ask_dest(stock):
    while True:
        dest = input('\nPlease enter your destination: ')
        dest = dest.lower()
        amount = int(input("How many tickets? "))
        # need input validation here if the amount is < 1.
        if stock[dest]['qty'] >= amount:
            sell(stock, dest, amount)
            break
        elif stock[dest]['qty'] < amount:
            print('Sorry, {}s are out of stock'.format(dest))
            break
        else:
            print("Sorry, we don't have that, look at the menu.")
            continue

def sell(stock, dest, amount):
    cost = amount * stock[dest]["price"]
    confirmation = input(f"Are you sure? That will be ${cost}. [Yes/No] ")
    if "yes" == confirmation.lower():
        stock[dest]["qty"] -= amount
        print(f"Purchase summary: Departure to {dest} at {stock[dest]['time']}. Please have your ticket ready at gate. Have a safe journey!")
        return stock
    # ask user if they would like to purchase again. if yes, then repeat from step 1 (print menu, and so on)

if __name__ == '__main__':
    stock = dict(cirebon=dict(code="TK001", time="08:30", qty=20, price=50000),
                 yogyakarta=dict(code="TK002", time="08:00", qty=25, price=100000),
                 surabaya=dict(code="TK003", time="13:00", qty=30, price=200000),
                 )
    name = input('What is your name? ')
    print(f'Hi, {name}. Here is the list of embarkment:')
    menu(stock)
    ask_dest(stock)