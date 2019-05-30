#def:声明方法的关键字;int_1:为自定义方法的名称;():下面写方法的内容
def int_1():
    # 生成一个变量,数据类型int(数值)类型; 前面变量名,后面变量值
    aint = 5
    #type(变量值)--->>获取数据类型或者变量类型;print(字符串)--->>将数据打印显示
    print(type(aint))
def str_1():
    # 生成一个变量,数据类型string(字符串)类型
    astr = '5'
    #type(变量值)--->>获取数据类型或者变量类型;print(字符串)--->>将数据打印显示
    print(type(astr))
def test1():
    print('test1')
def test2():
    print('test2')
def test3():
        print('test3')
# 全局变量--->>与方法平级;局部变量--->>在方法内部,只能在当前方法内使用
def float1():
    afloat = 6.6
    print(type(afloat))
# 字符串转换成数字类型
def type_zhuanhuan():
    b = '50'
    print(type(b))#打印b的类型为字段(str)
    print(type(int(b)))#打印b的类型从字段转换为int(整数)
# 数字转换成字符串类型
def type_zhuanhuan1():
    b = 50
    print(type(b))#打印b的类型为数字(int)
    print(type(str(b)))#打印b的类型从字段转换为字段(str)
# 数字转换成小数类型
def type_zhuanhuan2():
    b = 50
    print(type(b))#打印b的类型为数字(int)
    print(type(float(b)))#打印b的类型从字段转换为小数(float)

# 连接多个字符串和数字类型:print('%s%s'%(a,b)) 其中一个 %s 代表一个占位符,固定写法.
def str_join():
    a=123
    b='鱼'
    c='小蜜蜂'
    print('%s%s'%(a,b))
    print('%s  <・)))><<   %s <・)))><<    %s'%(a,b,c))
#方法括号里面的叫参数,多个参数用 , 分开
def add(num1,num2):
    print(num1)
    print(num2)
#方法执行到return,就返回return后面的值.
    return(num1+num2)
def add1(numb1,numb2):
    print(numb1)
    print(numb2)
    print(numb1+numb2)


# 这是main方法,可以直接执行,main方法下面不能有其他方法
if __name__ == '__main__':
    #打印
    print('Hello World')
    # 生成一个变量,数据类型int(数值)类型
    aint = 5
    # 生成一个变量,数据类型string(字符串)类型
    astr = '5'
    #type(变量值)--->>获取数据类型或者变量类型;print(字符串)--->>将数据打印显示
    a = add(10,20)
    b = add1(15,25)
    print('------------')
    print(a)
    print(b)
