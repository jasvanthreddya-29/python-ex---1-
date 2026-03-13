print("1.Check balance")
print("2.view offers")
print("3.special recharge")
print("0.exit")
choice = input("please enter your choice:")
if choice == '1':
    print("your balance is Rs.500")
elif choice == '2':
    print("you have new offers")
elif choice =='3':
    print("special recharge applied successfully.")
elif choice ==0:
    print("exiting")
else:
    print("invalid choice :")