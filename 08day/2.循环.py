import random
i = 0
while i < 3:
	player = int(input("请输入 1.石头  2.剪刀  3.布 :"))
	computer = random.randint (1,3) 
	if ((player == 1 and computer ==2) or (player == 2 and computer ==3) or (player == 3 and computer ==1)):

	    print("你赢了!")
	elif player == computer:
		print("平局")
	else:
		print("你输了！")
	i+=1
