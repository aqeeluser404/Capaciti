citi_burger = 0
citi_pie = 0
sausage_roll = 0
russian_roll = 0
small_chips = 0
big_chips = 0
coke = 0

def total(citi_burger, citi_pie, sausage_roll, russian_roll, small_chips, big_chips, coke):
    total_cost = (citi_burger * 22) + (citi_pie * 12) + (sausage_roll * 13) + (russian_roll * 20) + (small_chips * 20) + (big_chips * 10) + (coke * 9)

    if citi_burger > 0:
        print(f" CiTi burger: {citi_burger} x R22.00 = R{citi_burger*22}")
    if citi_pie > 0:
        print(f" CiTi pie: {citi_pie} x R12.00 = R{citi_pie*12}")
    if sausage_roll > 0:
        print(f" Sausage roll: {sausage_roll} x R13.00 = R{sausage_roll*13}")
    if russian_roll > 0:
        print(f" Russian roll and chips: {russian_roll} x R20.00 = R{russian_roll*20}")
    if small_chips > 0:
        print(f" Small chips: {small_chips} x R10.00 = R{small_chips*10}")
    if big_chips > 0:
        print(f" Big chips: {big_chips} x R20.00 = R{big_chips*20}")
    if coke > 0:
        print(f" Coke: {coke} x R9.00 = R{coke*9}")

    print("====================================================================")
    print(f" Total cost: R{total_cost}")


print("""
        1. CiTi burger              R22.00
        2. CiTi pie                 R12.00  
        3. Sausage/Russian roll     R13.00
        4. Russian roll and chips   R20.00  
        5. Small chips              R10.00
        6. Big chips                R20.00
        7. Coke (350ml)             R9.00
        8. Pay Now
        0. Exit
          """)

while True:

    order_list = int(input("What would you like to order?: "))

    if order_list == 0:
        break
    
    if order_list == 1:
        citi_burger += 1
    elif order_list == 2:
        citi_pie += 1
    elif order_list == 3:
        sausage_roll += 1
    elif order_list == 4:
        russian_roll += 1
    elif order_list == 5:
        small_chips += 1
    elif order_list == 6:
        big_chips += 1
    elif order_list == 7:
        coke += 1
    elif order_list == 8:
        total(citi_burger, citi_pie, sausage_roll, russian_roll, small_chips, big_chips, coke)
        break
    else: 
        print("Invalid Request, try again")
    



