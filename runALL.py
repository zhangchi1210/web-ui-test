# encoding: utf-8
from selenium import webdriver


def run():
    # 加启动配置
    option = webdriver.ChromeOptions()
    # 关闭“chrome正受到自动测试软件的控制”
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 不自动关闭浏览器
    option.add_experimental_option("detach", True)

    # 创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
    driver = webdriver.Chrome(options=option, executable_path="E:/04_script/zhangchi/web-ui-test/driver/chromedriver.exe")

    # 通过浏览器向服务器发送URL请求
    driver.get("http://10.4.2.191:8081/login")

    # 窗口最大化
    driver.maximize_window()


if __name__ == '__main__':
    run()
