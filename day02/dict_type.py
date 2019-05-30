adict = {"username":"admin","password":"123456"}

def dict_sel():
    #字典是无序的,只能通过key去访问value,key不能重复,注意方括号
    print(adict["username"])

def dict_update():
    adict['username']='hews'
    print(adict)

def dict_delect():
    a = adict.pop('username')
    print(adict)

def dict_add():
    adict['age']=25
    print(adict)
    bdict={'list' : [1,2,3],'tuple':(4,5)}
    adict.update(bdict)
    print(adict)

    cdict = {'password':'666','class':'1904'}
    ddict = dict(adict,**cdict)
    print(ddict)

def dict_zhuanhuan():
    print(type(adict))

# 题: 新建一个字典变量,里面有两个键值对,通过key访问一个值,删除一个键值对,
# 添加一个键值对,更改任意一个值,再新建一个字典,将两个合并
def dict_homework():
    bdict = {"studentid":"7","name":"hews"}
    print(bdict["studentid"])
    a=bdict.pop("studentid")
    print(bdict)
    bdict["class"] = 1905
    print(bdict)
    bdict["class"] = 1904
    cdict ={"gade":60,"teacher":"li"}
    ddict = dict(bdict,**cdict)
    print(ddict)
if __name__ == '__main__':
    dict_homework()

