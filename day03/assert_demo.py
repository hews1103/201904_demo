def assert_int():
    try:
        assert 5>4
        assert 3==3
        assert 2<6
    except:
        print('断言失败')

def assert_str():
    a=1
    b=[1,2]
    c=[2]
    try:
        assert a in b
        assert a==1
        assert c not in b
    except:
        print('断言失败')

if __name__ == '__main__':
    assert_int()
    assert_str()