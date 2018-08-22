import time
print("欢迎来到麒麟网咖".center(30,"$"))
list = []
all_money = 0
while True:
	print("1.上机")
	print("2.下机")
	print("3.管理")
	num = int(input("请选择功能："))
	if num == 1:
		d = {}
		card = input("请输入身份证号：")
		d["card"] = card
		d["time"] = int(time.time())
		d["sj"] = True
		list.append(d)
		print(list)
	elif num == 2:
		print("下机")
		card = input("请输入身份证号：")
		for i in list:
			if i["card"] == card:
				i["sj"] = False
				endtime = int(time.time())
				swq = (endtime-i["time"])*10
				print("上网花了%.02f"%swq)
				money = float(input("请输入金额，不找零！"))
				all_money += swq
				print("下机成功")
	elif num == 3:
		acount = input("请输入管理员账号：")
		pwd = input("请输入管理员密码：")
		if acount == "lirui" and pwd == "lirui":
			print("欢迎老板！")
			num = int(input("请选择功能："))
			count = 0
			if num == 1:
				print("今天上机%d"%len(list))
				for i in list:
					if i["sj"] == False:
						count +=1
				print("今天下机%d"%count)
				print("今天收益%.02f"%all_money)
