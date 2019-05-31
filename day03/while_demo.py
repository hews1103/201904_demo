def while_demo():
    a=0
    while a<6:
        print(a)
        a+=1

def try_demo():
    try:
        print('报错前')
        A=5/0
        print('报错后')
    except:
        print('报错了')
    print('1,2,3,4,5')
    
if __name__ == '__main__':
    try_demo()