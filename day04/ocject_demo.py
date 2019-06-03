class hello(object):
    def __init__(self,name,age,grade):
        self.name =name
        self.age =age
        self.grade =grade

    def e(self):
        print(self.name + '田')

    def r(self):
        print(self.age + 'һ')

    def t(self):
        print(self.grade + '一')

    def q(self):
        print('他的名字叫%s  ,今年%s岁了  ,他语文考了%s分  '%(self.name,self.age,self.grade))


class World(hello):
    def w(self):
        print(self.e())

    def t(self):
        print(self.grade +'橘子'+'香蕉')





if __name__ == '__main__':
        # v=hello('田鱼','16','80')
        # v.q()
        # v.r()
        # v.e()
        world =World('鱼','20','20')
        world.q()
        world.t()
        print(world.name)

