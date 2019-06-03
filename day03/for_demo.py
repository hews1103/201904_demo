def for_demo():
    for i in range(3):
        print(i)
        print('hello')



def for_demo1():
    for i in range(3,7):
        print(i)
        print('hello')

def for_demo2():
    for i in range(0,50,1):
        if i%2==1:
            return(i)
        print(i)


def for_demo3():
    for i in range(20,2,-2):
        print(i)
        print('hello')

def for_demo4():
    a=[7,8,9,6,5,4]
    for i in a:
        print(i)

    for i in range(len(a)):
        print(a[i])


def for_demo5():
    for i in range(5):
        print('Hello',end='冷酷追击')
        print(i)
        for j in range(3):
             print('World')
             print(j)
        print('\n')

def for_demo6():
    for i in range(5):
        if i ==2:
            break
        print(i)
def for_demo7():
    for i in range(5):
        if i ==2:
            continue
        print(i)

if __name__ == '__main__':
    for_demo3()
