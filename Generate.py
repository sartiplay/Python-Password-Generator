import time
import random
import sys
from config import *

hasArgs = False; #For checking that user add's Arguments

#Check For Arguements | if no Arguements [Reload Script!]
try:
  INARGS = sys.argv[1]
  hasArgs = True
except:
  print("Argument Required, type in -h for help!")

#Check For Arguements | if no Arguements [Reload Script!]
try:
  INARGS2 = sys.argv[2]
  PASSWORD_LENGHT = int(sys.argv[2])
except:
  print()
  
#Save the File to the Same Directory as the Generate.py file
def Save_File(PW):
  with open("PasswordOUT.txt", "w") as f:
    f.write(f"GENERATET PASSWORD : {PW}")
    f.close()
    time.sleep(1)

#Ask the USER to Save the file to the System ( OPTIONS : YES | NO (Y/n))
def User_Save_Prompt(EXPW):
  print("Password Generatet!")
  USERIN = input("Do you want to Save it to a file Y/n : ")
  if(USERIN == "Y"):
    print("Saving File to System!")
    Save_File(EXPW)
  elif(USERIN == "n"):
    print("Not Saving File to System!")
  else:
    print("Please Input the Right Arguments (Y/n)")
    RePrompt(EXPW)


#Reload the User_Save_Prompt Prompt
def RePrompt(PW):
  User_Save_Prompt(PW)

#Generate the Password without Numbers
def NoNumbers():  
  i = 0
  preSAVE = ""
  while(i != PASSWORD_LENGHT):
    preSAVE += ALL_COMBINED_NO_NUMBERS[random.randrange(0, len(ALL_COMBINED_NO_NUMBERS))]
    i = i + 1
  RESULT = preSAVE
  print(RESULT)
  User_Save_Prompt(RESULT)

#Generate the Password without Symbols
def NoSymbols():  
  i = 0
  preSAVE = ""
  while(i != PASSWORD_LENGHT):
    preSAVE += ALL_COMBINED_NO_SYMBOLS[random.randrange(0, len(ALL_COMBINED_NO_SYMBOLS))]
    i = i + 1
  RESULT = preSAVE
  print(RESULT)
  User_Save_Prompt(RESULT)

#Generate the Password with everythin activated
def all():  
  i = 0
  preSAVE = ""
  while(i != PASSWORD_LENGHT):
    preSAVE += ALL_COMBINED[random.randrange(0, len(ALL_COMBINED))]
    i = i + 1
  RESULT = preSAVE
  print(RESULT)
  User_Save_Prompt(RESULT)


#Check the python Arguments [python3][python] | Generate.py | [Arg1][Arg2/Optional]
if(hasArgs):
  if(INARGS == "-nN"):
    NoNumbers()
  elif(INARGS == "-nS"):
    NoSymbols()
  elif(INARGS == "-a"):
    all()
  elif(INARGS == "-h"):
    print("AVAIABLE COMMANDS!\n-a for Big and Small Letters + Numbers and Symbols\n-nN for No Numbers\n-nS for no Symbols\n\nArg[2] : Second Argument can be Empty or can be a Number for the Length of the Password 'Standart Password Length : 10'\nExample : ( python3 Generate.py -a 15 )\n[python3][python] | Generate.py | [arg1] | [arg2/optional]")
  else:
    print(f"{INARGS} : is not a Valid Argument!!, \n Type in -h for Help")
    
    


