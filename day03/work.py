# 0到50的基数相加
# def work(a):
#     if a%2==1:
#         b=a
#         return b
#     else(b==b+1)%2==1:
#         print(b)
#         print(a+b)
def work1():
    sum=0
    for i in range(1, 51):
        if i % 2 == 1:
            sum=i+sum
    print(sum)

# 打印九九乘法表
def work2():
    for i in range(1,10):
        for j in range(1,i+1):
            print('%s * %s = %s'%(j,i,i*j),end='    ')
        print('')



        # x = i + 1
        # for j in range(1,10):
        #     z=i*j
        #     y=('%s*%s=%s'%(i,j,z))
        #     print(y)
        #     if i==j:
        #         continue
        # print('\n')
'''
每次拿 4 个 最后剩一个, 
每次拿五个剩四个,
每次拿6个 最后剩3个,
每次拿七个最后剩5个,
每次拿八个最后剩一个,
每次拿九个 刚好拿完, 篮子最多放1000个鸡蛋,求有多少鸡蛋
'''
def homework():
    for a in range(1,1001):
        if a%4==1:
            if a%5==4:
                if a%6==3:
                    if a % 7 == 5:
                        if a % 8 == 1:
                            if a % 9 == 0:
                                print(a)



if __name__ == '__main__':
    homework()