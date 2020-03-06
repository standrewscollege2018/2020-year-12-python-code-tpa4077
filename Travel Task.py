destinations = [["Sydney", 326], ["Tonga", 378], ["Shanghai", 1436], ["London", 2376]]
stay = [["Sydney", 120], ["Tonga", 40], ["Shanghai", 60], ["London", 80]]


def plan():
    flight_cost = 0
    stay_cost = 0
    print("Where are you departing from? \n 1: Auckland \n 2: Wellington \n 3: Christchurch")
    depart_choice=input()
    if depart_choice == "1":
        cost += 0      
    elif depart_choice == "2":
        cost += 50
    elif depart_choice == "3":
        cost += 75     
    else:
        print("invalid input \n")
    print("Where is your Intended Destination? \n 1: Sydney \n 2: Tonga \n 3: Shangai \n 4: London")
    dep=int(input())
    cost += destinations [dep-1] [1]
    
    
    

menu = True

while menu==True:
    print("Welcome to Tob.Ravel \n 1: Plan a Flight \n 2: View Prices")
    menu_choice=input()
    if menu_choice == "1":
        plan()
    elif menu_choice == "2":
        View()
    else:
        print("Error invalid input \n")
    




    
