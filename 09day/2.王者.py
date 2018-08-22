
a = 0
while a < 10:
	one = int(input("请输入账号："))
	two = int(input("请输入密码："))
	if (one == 123456 and two == 123456):
		break
	a += 1
print("登陆成功！")
y = 0
while y < 3:
	x = int(input("请选择 1,ADC 3,肉盾 3，法师："))
	if x == 1:
		print("鲁班七号")
	elif x == 2:
		print("亚瑟")
	elif x == 3:
		print("貂蝉")
	else:
		print("???????")
	y += 1
