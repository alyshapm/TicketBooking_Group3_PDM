from class_ticket_PDM import Ticket

# print list of train names, dest and price and code
print("Code \tTrain name \tDestination \tPrice")
print("--------------------------------------------------")
print("TK001 \tGajayana \tCirebon \tRp.50,000")
print("TK002 \tBima \t\tYogyakarta \tRp.100,000")
print("TK003 \tArgo Bromo \tSurabaya \tRp.200,000")

while True:
    destination = input("Hello, please enter destination: ")
    if destination == "Cirebon" or "Yogyakarta" or "Surabaya":
        break
    else:
        destination = input("Re-enter valid destination: ")

while True:
    numTicket = int(input("Enter number of ticker: "))
    if numTicket < 1:
        numTicket = int(input("Re-enter valid number of ticket: "))
    else:
        break

tix = Ticket(destination, numTicket)


# function to validate 