details = {"Ravi":1234,"Kumar":5678,"Siva":1998}
pin_no = int(input("Enter Your PIN :"))
for key,values in details.items():
    if pin_no== values:
        print("Welcome Mr/Miss :",key)
        balance = {"Ravi": 100000, "Kumar": 200000, "Siva": 500000}
        for x,y in balance.items():
            if key==x:
                print("Available Balance in your Account is:",y)
                amount = int(input("Enter Your Withdrawall Amount:"))
                if amount % 100 == 0:
                    if amount <= 20000:
                        if amount <= y:
                            print(amount,"is Withdrawall")
                            y -= amount
                            print("Current Balance = ", y)
                        else:
                            print("Funds Not Available")
                    else:
                        print("Max withdraw Amount is 10000/- Only")
                else:
                    print("Invalid Amount")
            elif pin_no != values:
               print("Invalid PIN")
print("Thanks")