#define a function to repeat the calculator
def repeat():
  restart = input("\nDo you want to try again? (y/n): ")
  #while loop for the user's 'yes' choice 
  if restart == 'y':
    calc()
  else:
    print("===============")
    print("    Good bye")
    print("===============")
#defined a function for the calculator to run
def calc ():
  print ("---------------------")
  print ("My Desktop Calculator")
  print ("     by Karla Alvarez")
  print ("---------------------")
  print ("")
  
  
  nam1 = input("Enter your name:>  ")
  
  num1 = float(input("Enter a number:>  "))
  num2 = float(input("Enter another number:>  "))
  
  print ("")
  print ("===================")
  print ("  Calculator Menu")
  print ("===================")
  print ("")
  print ("  1. Add")
  print ("  2. Subtract")
  print ("  3. Multiply")
  print ("  4. Divide")
  print ("  5. Remainder")
  print ("")
  print ("===============")
  choice = input("Make a selection (1 - 5):>  ")
  
  if choice < "1" or choice > "5":
   print (nam1, ", you entered a wrong choice")
  elif choice == '1':
   print (nam1, "...here is the answer")
   print (num1, "+", num2, "= ", num1+num2) 
  elif choice == '2':
   print (nam1, "...here is the answer")
   print (num1, "-", num2, "= ", num1-num2) 
  elif choice == '3':
   print (nam1, "...here is the answer")
   print (num1, "*", num2, "= ", num1*num2) 
  elif choice == '4':
   if num2 == 0:
    print ("OOPS!", nam1, "...we can not divide by zero(0)")
   else:
    ans = num1/num2
    print (num1," / ", num2, " = ",format(ans, '.2f'))
  elif choice == '5':
    if num2 == 0:
      print ("OOPS!", nam1, "...we can not divide by zero(0)")
    else:
        print (num1, "%", num2, "= ", num1%num2) 
  print ("")
  repeat()

calc()




    
        
  
