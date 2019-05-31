avar='Hello'
def d1():
    global avar
    avar='你好'

def d2():
    print(avar)

def d3():
    bvar='world'
    print(bvar)

def d4():
    try:
        print(bvar)
    except:
        print('失败')

if __name__ == '__main__':
    d2()
    d1()
    d2()
    d3()
    d4()