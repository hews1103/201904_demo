import allure

@allure.feature('订单模块')
class Test_order(object):

    @allure.story('下订单')
    def test_order_add(self):
        # 假设发送了请求
        # 假设获得了响应
        assert '成功' in '操作成功'

    @allure.story('待发货')
    def test_order_demo(self):
        # 假设发送了请求
        # 假设获得了响应
        try:
            assert '雨女' in '雨女无瓜'
        except:
            print('响应错误')