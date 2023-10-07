hight=int(input("enter your hight here:- "))
bill=0
if hight>=3:
    print("you can ride")
    age=int(input("enter your age here:- "))
    if age<12:
        bill=100
        print("ticket price is 100")
    elif age<18:
        bill=200
        print("ticket price is 200")
    else:
        bill=450
        print("ticket price is 450")
    photo=(input("you want to take pic : (y/n)? ") ) 
    if photo == 'y' or photo == 'n':
        bill=bill+50
    print(f"your total price is : {bill}")



else:
    print("you cant ride")