alist = ['星期四',2,'你好',5,6,7]
blist=[1,2,3,'4']
clist=[5,6,7]
dlist=[1,2,3,4,5,6,8,9]

#1.访问list--->>变量名[索引]  注意方括号
def list_sel():
    # 通过索引访问
    print(alist[0])
    #访问第三位
    print(alist[2])
    #通过切片访问
    print(alist[2:3])
    #访问从第五个开始到后面所有
    print(alist[4:])
    #将索引倒序
    print(alist[::-1])
    #取索引后三位
    print(alist[-3:])
    #取索引后三位,并倒序
    print('-----------')
    print(alist[:2:-1])
#2.删除list中的元素--->>变量名.pop(索引)
def list_del():
    #调用删除方法,不填写参数,默认删除最后一位
    alist.pop()
    print(alist)
    #调用删除方法,填写参数,参数为索引值--->>可以删除指定元素
    a=alist.pop(2)
    print(alist)
    #调用删除元素进行返回
#3.增加list中的元素--->>
def list_add():
    # 增加元素在列表末尾
    blist.append(5)
    blist.append('Hello World')
    print(blist)
    #合并两个集合中的元素
    blist.extend(clist)
    print(blist)
#4.更新列表中的元素
def list_update():
    alist[2] = 'Hello'
    print(alist)
    alist[2] = 200
    print(alist)
#5.排序
def list_orderby():
    #默认 模块.sort() 为正序;
    dlist.sort()
    print(dlist)
    # 模块.sort(reverse=Ture)为倒序
    dlist.sort(reverse= True)
    print(dlist)
#6.去重
def list_distinct():
    elist = [1, 2, 2, 3, 3, 5, 4, 4]
    elist=list(set(elist))
    print(elist)
#7.获取列表长度
def list_length():
    print(len(dlist))

# 练习题:新建一个list变量,里面有五个元素,
# 访问索引2,切片范根索引1到4,删除索引3,
# 添加两个元素,第0位元素改成字符5,获取索引长度
def list_t():
    tlist = [1,2,3,4,5]
    xlist = [6,7]
    print(tlist[2])
    print(tlist[1:4])
    print(tlist.pop(3))
    tlist.extend(xlist)
    print(tlist)
    tlist[0]='5'
    print(tlist)
    print(len(tlist))


if __name__ == '__main__':
    list_t()
    print('---------')
