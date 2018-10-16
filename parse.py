

f = open("目录.txt")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
alldata = []
while line:
    alldata.append(line.split(' '))
    line = f.readline()
f.close()

print(alldata)

def getName(cid:str):
    for item in  alldata:
        if item[1]==cid:
            return item[0]

print(getName('253455'))


string ='http://www.leleketang.com/let3/knowledge_list.php?cid=253455\n'
print(string[-7:-1])