d = {"name":"李瑞雄","sex":"男","mz":"汉","age":28,"abbress":"北京","num":"411381200104161234"}
#增加
d["edu"] = "博士"
print(d)
#修改
d["sex"] = "汉子"
#删除
d.pop("name")
print(d)
#del d ["name"]
print(d)
#查
#print(d["name"]) 没有会报错
print(d.get("name")) #没有键返回none
