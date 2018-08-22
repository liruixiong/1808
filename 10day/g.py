l = ["老王","老宋","老赵"]
for i in l:
	print(i)

list = []
for i in range(5):
	grade = float(input("请输入成绩："))
	list.append(grade)
for i in list:
	print(i)
list.sort()
print(list)
