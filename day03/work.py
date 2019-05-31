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
    
        # x = i + 1
        # for j in range(1,10):
        #     z=i*j
        #     y=('%s*%s=%s'%(i,j,z))
        #     print(y)
        #     if i==j:
        #         continue
        # print('\n')






if __name__ == '__main__':
    work2()