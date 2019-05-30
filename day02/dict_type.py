adict = {"username":"admin","password":"123456"}

def dict_sel():
    #字典是无序的,只能通过key去访问value,key不能重复,注意方括号
    print(adict["username"])

if __name__ == '__main__':
    dict_sel()