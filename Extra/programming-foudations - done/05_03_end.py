def wash_car(amount_paid):
    print("Vai receber: ")
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

money = input("Quanto voce vai pagar? ")
wash_car(int(money))