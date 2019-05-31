def open_demo():
    tese=open('test.txt','w+')
    for i  in range(6):
        tese.write('德玛西亚\n')

def open_demo1():
    test =open('test.txt','a+')
    for i  in range(6):
        test.write('艾欧尼亚\n')

def open_demo2():
    test = open('test.txt', 'r')
    print(test.readlines())

if __name__ == '__main__':
    open_demo2()