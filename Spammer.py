import pyautogui as pt              #pip install pyautogui 
import time                         #pip install time
import os
import pyfiglet                     #pip install pyfiglet
from progress.bar import Bar        #pip install progress.bar


os.system("cls")
os.system("color 4")
T = "Welcome To Spammer $V3N0M Edition"   #Front
ASCII_ART_T = pyfiglet.figlet_format(T) 
print (ASCII_ART_T)
print ("---" * 20)
print ("Done by Wadee-_-Haddad")
print ("---" * 20)
print("""                                                                                                    
              .:^^^^:.                                              
         ^JB&@@@@@@@@@@&#5~.                                        
      .5&@@@@@@@@@@@@@@@@@@@B^                                      
     Y@@@@@@@@@@@@@@@@@@@@@@@@#:                                    
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@?                                   
   #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@7                                  
  J@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                  
 .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@7                                 
 7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P     _  __     __ _____  _   _   ___   __  __                         
 G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B    | | \ \   / /|___ / | \ | | / _ \ |  \/  |                        
 #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#   / __) \ \ / /   |_ \ |  \| || | | || |\/| |                        
 B@@G#&@@@@@@@@@@@@@@@@@@@@@&#BG&@G   \__ \  \ V /   ___) || |\  || |_| || |  | |                        
 !@@   .~Y#@@@@@@@@@@@@@&Y^.   .@@~   (   /   \_/   |____/ |_| \_| \___/ |_|  |_|                        
  B@B      .5@@@@@@@@@#^      :&@B     |_|                        
   #@#.      .B@@@@@@J       ?@@&                                   
    B@@P:      G@@@@?     .J&@@&.                                   
     J@@@&G?^:..@@@&..^?P&@@@@G                                     
      :&@@@@@@@@@@@@@@@@@@@@@7                                      
        J@@@@@@@@@@@@@@@@@@B.                                       
         .P@@@@@@@@@@@@@@#~                                         
           .Y&@@@@@@@@@G^                                           
              :75GGPJ^""")

limit = input("Enter Message limit ;) ==> ")   #input limit
print ("==============Adding Limit==============")
message = input("Enter Message ==> ")          #input message

bar = Bar('Processing', max=20)                #Front
for i in range(5):
    time.sleep(0.1)
    bar.next()
bar.finish()

bar1 = Bar('Processing', max=20)
for i in range(10):
    time.sleep(0.1)
    bar1.next()
bar1.finish()

bar2 = Bar('Processing', max=20)
for i in range(15):
    time.sleep(0.1)
    bar2.next()
bar2.finish()

bar3 = Bar('Processing', max=20)
for i in range(20):
    time.sleep(0.1)
    bar3.next()
bar3.finish()

i = 0

time.sleep(5)                #sleep to not get time out or ban

while i < int(limit):      #loop 
    pt.typewrite(message)       
    pt.press("enter")
    i+=1
