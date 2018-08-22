list = []
for i in range(2):
	d = {}
	name = input("请输入名字：")
	age = input("请输入年龄：")
	sex = input("请输入性别：")
	d["name"] = "name"
	d["age"] = "age"
	d["sex"] = "sex"
	print(d)
	list.oppend(d)
print(list)
for i in list:
	for j in i.valuse():
		print(j)
