"""
list = ["哈","a","w"]
for p,i in enumerate(list):
	print(p,i)
"""


list = [{"北京":{"面积":"1000平","人口":"200W"},"上海":{"面积":"600平","人口":"150W"}}]
for i in list:
	print(i)
	for k,v in i.items():
		for j,l in v.items():
			print(k,j,l)
