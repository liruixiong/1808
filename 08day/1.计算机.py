x = float(input("请输入x："))
ply = input("请输入 +，-，*，/，** ：")
y = float(input("请输入Y："))
a = x+y
b = x-y
c = x*y
d = x/y
e = x**y

if ply == "+":
	print(a)
elif ply =="-":
	print(b)
elif ply =="*":
	print(c)
elif ply =="**":
	print(e)
else:
	print(d)
