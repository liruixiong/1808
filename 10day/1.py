i = 1
while i <= 3:
	import random
	on = int(input("请输入 1.石头 2.剪刀 3.布："))
	cm = random.randint(1,3)
	if ((on == 1 and cm == 2)or(on == 2 and cm == 3)or(on == 3 and cm == 1)):
		print("你赢了！！")
	elif on == cm:
		print("平局")
	else:
		print("你输了！")
	i+=1
