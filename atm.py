import os
import random
import time
print('Welcome to SBI BANK in idupulapaya\n')
print('what can i do for u?\n')
restart=('y')
chances=4
balance=10000
while chances>=0:
    pin=int(input('pls,enter ur pin no.r\n'))
    if pin == (3456):
       print('------ur pin is correct------\n')
       while restart not in ('n','NO','no','N'):
             print('1.know ur balance\n')
             print('2.withdraw ur money\n')
             print('3.cash to pay\n')
             print('4.cash to return the card\n')
             print('5.transfer the money to another account\n')
             print('6.recharge to my mobile\n')
             option=int(input('select what u want to choose'))
             if option==1:
                print("u have the account balance is:",balance)
                restart=raw_input("would you like to countinue")
                if restart in("n","no","No","N"):
                   print("thank you\n")
                   break
             elif option==2:
                     option2=('y')
                     withdraw=float(input('how much would you like to withdraw?\n10/-20/-,40/-,60/-,80/-,100/-,1000/-,2500/-'))         
                     if withdraw in [10,20,30,40,50,100,1000,2500]:
                        balance=balance-withdraw
                        print('u have the account balance is:',balance,'\n')
                        restart=raw_input('would you like to countinue\n')
                        if restart in('n','no','No','N'):
                              print('thank you\n')
                              break    
                     elif balance>0:
                           print('u donot have that much of amount in ur account\n')
                           restart=raw_input('would you like to countinue\n')
                           if restart in('n','no','No','N'):
                              print('thank you\n')
                              break

             elif option==3:
                      pay_in=float(input('How much u want to pay\n'))
                      if pay_in in [10,20,30,40,50,100,1000,2500]:
                         balance=balance+pay_in
                         print('u have the account balance is:\n',balance,'\n')         
                         restart=raw_input('would you like to countinue\n')
                         if restart in('n','no','No','N'):
                            print('thank you\n')
                            break
             
             elif option==4:
                           print('Please wait whilst your card is Returned...\n')
                           print('Thank you for you service\n')
                           restart=raw_input('would you like to countinue\n')
                           if restart in('n','no','No','N'):
                              print('thank you\n')
                              break
             elif option==5:
                  option5=('y')
                  acnumber=int(input('enter the bank account no.r u want to transfer\n'))
                  if acnumber == (1234567890):
                     acnumber=int(input('how much u want to transfer\n'))
                  if acnumber in [10,20,30,40,50,100,1000,2500]:
                     balance=balance-acnumber
                     print('u have the account balance is:\n',balance,'\n')
                     print('the amount is transfered successfully\n')
                     restart=raw_input('would you like to countinue\n')
                     if restart in('n','no','No','N'):
                                 print('thank you\n')
                                 break
             elif option==6:
                  option6=('y')
                  phnumber=int(input('enter ur mobile no.r\n'))
                  if phnumber == (9822334456):
                     phnumber=int(input('how much u want to transfer\n'))
                     if phnumber in [10,20,30,40,50,100,1000,2500]:
                               balance=balance-phnumber
                               print('u have the account balance is:\n',balance,'\n')
                               print('the amount is transfered to ur mobile successfully\n')
                               restart=raw_input('would you like to countinue\n')
                               if restart in('n','no','No','N'):
                                   print('thank you\n')
                                   break
             else:
                 print('enter the correct pin no.r\n')
                 restart=('y')
       break 
    elif pin != ('3456'):
        print('Incorrect Password')
        chances = chances - 1
        if chances == 0:
            print('\nNo more tries')
            break
print("\nBY MANASA J\n")
                     
