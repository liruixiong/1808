print("欢迎来倒学籍管理系统".center(30,"*"))
box = []
while True:
	print("1，录入")
	print("2，修改")
	print("3，查找")
	print("4，删除")
	print("5，退出")
	num = int(input("请选择功能："))
	if num == 1:
		xjb = {}
		name = input("请输入姓名：")
		age = int(input('请输入年龄：'))
		sex = input('请输入性别：')
		phone = input('请输入手机号：')
		xjb['name'] = name
		xjb['age'] = age
		xjb['sex'] = sex
		if phone.startswith("1") and len(phone) == 11:
			xjb['phone'] = phone
		else:
			print("输入有误，请重输")
			continue
		box.append(xjb)
		print(box)
	elif num == 2:
		name = input("请输入要修改的名字：")
		for xjb in box:
			if xjb ["name"] == name:
				print(xjb)
				print("1.修改名字")
				print("2.修改年龄")
				print("3.修改性别")
				print("4.修改手机号")
				num = int(input("请选择修改内容："))
				if num == 1:
					um = input("请输入修改内容：")
					xjb["name"] = um
				elif num == 2:
					om = int(input("请输入要修改的年龄："))
					xjb["age"] = om
				elif num == 3:
					im = input("请输入要修改的性别：")
					xjb["sex"] = im
				elif num == 4:
					ym = int(input("请输入要修改的手机号："))
					xjb["phone"] = ym
				print("修改成功")
				print(xjb)
			else:
				print("没有这个人")
				break
	elif num == 3:
		mor = input("请输入要查找的名字：")
		for xjb in box:
			if xjb["name"] == mor:
				print("姓名\t年龄\t性别\t手机号")
				print("%s\t%s\t%s\t%s"%(xjb["name"],xjb["age"],xjb["sex"],xjb["phone"]))
			else:
				print("没有这个人")
	elif num == 4:
		name = input("请输入要删除的名字：")
		for xjb in box:
			if xjb["name"] == name:
				nom = int(input("是否要删除 1:yes  2:no ："))
				if nom == 1:
					box.remove(xjb)
			else:
				print("没有这个人")
			break
	elif num == 5:
		print("退出")
		break
