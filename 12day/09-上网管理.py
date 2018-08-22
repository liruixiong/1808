

import time
print("欢迎来到起麒麟网咖".center(30,"$"))
box = []
while True:
	print("1.上机")
	print("2.下机")
	print("3.管理")
	num = int(input("请选择功能："))
	if num == 1:
		d = {}
		card = int(input("请输入身份证号："))
		money = float(input("请输入金额："))
		d["card"] = card
		d["money"] = money
		d["time"] = int(time.time())
		box.append(d)
		print("登陆成功!!!")
		print(box)
	elif num ==2:
		card = input("请输入身份号：")
		for i in box:
			if d["card"] == card:
				endtime = int(time.time())
				diff_money = (enditime-i["time"])*10
				diff = i["money"] - diff_money
				print("上网共花费了%.02f元，还剩%.02f元"%(diff_money,diff))
	elif num == 3:
		account = input("")
