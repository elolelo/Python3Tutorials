import time 
import random

answer1 = ["1"]
answer2 = ["2"]
answer3 = ["3"]
yes = ["Y", "y", "yes, yebo"]
no = ["N", "n", "no, Nah"]

corona_person = 0
stranger = 0

required = ("\n Please answer using  1, 2 or 3 \n") 


def print_with_delay():
  print ("During the time of Covid-19, it happens that there are restrictions of only a maximum of 50 people sharing an enclosed building. You want to join to rest of you crew in a hall but you don't know how many people are inside already.You are waiting outside looking inside the hall building through the window. You want to enter the building but at the same time you don't want to break the restriction rules.")
  time.sleep(1)
  print ("""  1. Do you enter anyway because it looks empty
  2. Do you feel safe enough to enter and be with your crew even though it looks full
  3. Do go back to your home """)
  choice = input("YOUR ANSWER: ") 
  if choice in answer1:
    option_enter()
  elif choice in answer2:
    print ("\nThe building is full , you are breaking Covid-19 restrictions. You get Corona and you will die!  "
    "\n\nYou Lost!!")
  elif choice in answer3:
    option_run()
  else:
    print (required)
    print_with_delay()

def option_enter(): 
  print ("\n You realise that you dont's have your mask on, do you: ")
  time.sleep(1)
  print ("""  1. Go wear mask and come back
  2. Turn your scarf into a mask and enter the building
  3. Change your mind and decide to go back home""")
  choice = input("YOUR ANSWER: ")
  if choice in answer1:
    option_run()
  elif choice in answer2:
    print ("\nYour scarf is stucked around your neck and you can't move it! So you can't cover your nose and mouth and you can'e enter the building." 
    "\n\nYou Lost!!")
  elif choice in answer3:
    option_cave()
  else:
    print (required)
    option_enter()

def option_cave():
  print ("\n You are thinking about a lot of things. Are you sure you want to go back home? "
  " Y/N?")
  choice = input("YOUR ANSWER: ")
  if choice in yes:
    corona_person = 1 
  else:
    corona_person = 0
  print ("\nWhat do you do next?")
  time.sleep(1)
  print ("""  1. Stop and not help the stranger
  2. Help the stranger
  3. Run away""")
  choice = input("YOUR ANSWER: ")
  if choice in answer1:
    print ("\n The strander infected you with corona \n\nYou Lost!!")
  elif choice in answer2:
   if corona_person > 0:
    print ("\nOn your way back home, you don't meet anyone and get home safe."
    "its chest. \n\nYou did not get or spread the corona virus!")
   else: 
     print ("\n  \n\nYou Lost!!")
  elif choice in answer3:
    print ("You did not get or spread the corona virus!")
    option_run()
  else:
    print (required)
    option_cave()

def option_run():
  print ("\n On your way back home to get mask you notice that you are hungry, "
  "Do you:")
  time.sleep(1)
  print ("""  1. Eat , take your mask and go back
  2. Buy food then join your crew
  3. Give up joining the crew and go back""")
  choice = input("YOUR ANSWER: ")
  if choice in answer1:
    print ("There is no food and you end up not having energy to go back."
    "\n\nYou Lost!!")
  elif choice in answer2:
    print ("\n You have no money to buy food and you end up not having energy to go back"
    "\n\nYou Lost!!")
  elif choice in answer3:
    option_town()
  else:
    print (required)
    option_run()
    
def option_town():
  print (
  "You are thinking about a lot of things. Are you sure you want to go back home? Y/N")
  choice = input("YOUR ANSWER: ")
  if choice in yes:
    stranger = 1 
  else:
    stranger = 0
  print ("As you are thinking ...")
  time.sleep(1)
  if stranger > 0:
    print ("\nYou have made a good decision!"
    "\n\n You get to your home without catching corona, you have won!!")
  else: 
     print ("\n You meet the  stranger  and you get contaminated you with the corona. "
     "\n\nYou Lost!!")

print_with_delay()