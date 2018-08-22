for i in range(3):
	account = input("请输入账号：")
	pwd = int(input("请输入密码："))
	if account !="laowang"or pwd != 123456:
		if i ==2:
			print("账号已被冻结")
		else:
			print("请重新输入")
	else:
		num = int(input("请选择 1-ADC 2-肉 3.法师："))
		if num == 1:
			print("鲁班七号")
		elif num ==2:
			print("亚瑟")
		elif num ==3:
			print("妲己")
		else:
			print("输入有误")
		break
