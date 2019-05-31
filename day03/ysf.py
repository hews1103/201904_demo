def deng(a):
    a=a+1
    print(a)
    a+=1
    print(a)
    a-=1
    print(a)
    a*=3
    print(a)
    a/=7
    print(a)

def for_demo(i):
    i+=1
    for i in range(3):
        print(i)
        print('hello')

if __name__ == '__main__':
    for_demo()