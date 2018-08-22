pwd = 123
omae = '123'
mo = 500

pw = int(input("请输入账号："))
om = input("请输入密码：")
if pw == pwd and om == omae:
	print("登陆成功")
	m = float(input("请输入取款金额"))
	if m > mo:
		print("余额不足")
	else:
		print("取款成功")
else:
	print("账号或密码错误")
