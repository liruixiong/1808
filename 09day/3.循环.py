import random
for i in range(1,4):
	pl = int(input("请输入 1.石头  2.剪刀  3.布："))
	co = random.randint(1,3)
	if ((pl == 1 and co == 2) or (pl == 2 and co == 3) or(pl == 3 and co == 1)):
		print("你赢了！")
	elif pl == co:
		print("平局")
	else:
		print("你输了")
	print(i)
