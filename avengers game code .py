import random
def  check(comp, user):
	 if(comp==user):
	 	return 0
	 elif(comp == 0 and user >0):
	 	return -1
	 elif(comp==1 and user >1):
	 	return -1
	 elif(comp==2 and user >2):
	 	return -1
	 elif(comp==3 and user >3):
	 	return -1
	 elif(comp==4 and user >4):
	 	return -1
	 elif(comp==5 and user >5):
	 	return -1
	 elif(comp==6 and user >6):
	 	return -1
	 elif(comp==7 and user >7):
	 	return -1
	 elif(comp==8 and user <8):
	 	return 1
	 else :
	 	return 1
comp=random.randint(0,8)
user  =int(input("0 for Thor , 1 for Wanda, 2 for captain marvel , 3 for captain america , 4 for Iron Man , 5 for Doctor Strange , 6 for Spiderman , 7 for Black Panther , 8 for Hulk:\n"))

score = check(comp,user)
print("You:", user)
print("Computer:", comp)



if score ==0:
	print("Its a draw")
elif score == -1:
	print("You Lose")
else:
	print("You Won , THE BEST AVENGER👑")