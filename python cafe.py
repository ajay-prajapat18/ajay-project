
import os 
menu = {'pizza' : 200, 'burger': 100 , 'pasta': 150, 'coffee':200,}


while True:
    total=0
    os.system( 'cls' if os.name =='nt' else 'clear')
    print("\t WELCOME TO PYTHON CAFE ")
    print(" PIZZA - 200\nBURGER - 100\nPASTA - 150\nCOFFEE - 200")
    first_order=input("\n\nWhat will you order :")
    if first_order in menu:
        total +=menu[first_order]
        
    else:
        print("Sorry! , We do not serve this dish")
    req = input("What will you order something else (yes/no) : ")
    if req=='yes':
        second_order = input("\n\nWhat your another order : ")
        if second_order in menu:
            total +=menu[second_order]

    print("YOUR TOTAL PAYABLE BILL -- " , total )
    again=input("Do you want to order again : ")
    if again !='yes':
        break








