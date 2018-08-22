print("欢迎来到学籍管理中心".center(30,"*"))
box = []
while True:
	print("1.录入")
	print("2.修改")
	print("3.查找")
	print("4.删除")
	print("5.退出")
	num = int(input("请选择功能："))
	if num == 1:
		print("录入")
	elif num == 2:
		print("修改")
	elif num == 3:
		print("查找")
	elif num == 4:
		print("删除")
	elif num == 5:
		print("退出")
		break
