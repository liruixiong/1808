a = 1
while a <=3:
	import random
	pl = int(input("请输入 1.石头 2.剪刀 3.布："))
	mo = random.randint(1,3)
	if((pl == 1 and mo == 2) or (pl == 2 and mo == 3 ) or (pl ==3 and mo == 1)):
		print("你赢了！")
	elif pl == mo :
		print("平局")
	else:
		print("你输了")
	a +=1
