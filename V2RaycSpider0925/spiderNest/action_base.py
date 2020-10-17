import random
import time
from datetime import datetime, timedelta
from string import printable

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from config import CHROMEDRIVER_PATH
from MiddleKey.VMes_IO import save_login_info


class BaseAction(object):
    """针对STAFF机场的基准行为"""

    def __init__(self, silence=True, anti=True, email_class='@qq.com', life_cycle=1):
        """
        设定登陆选项，初始化登陆器
        :param silence: （默认使用）为True时静默访问
        """

        # 初始化注册信息
        self.username, self.password, self.email = self.generate_account(email_class=email_class)

        # 信息共享v2ray订阅链接
        self.subscribe = ''

        # 初始化浏览器
        self.silence, self.anti = silence, anti

        # self.api = self.set_spiderOption()

        self.register_url = ''

        self.life_cycle = self.generate_life_cycle(life_cycle)

    @staticmethod
    def generate_account(email_class: str = '@qq.com'):
        """
        :param email_class: @qq.com @gmail.com ...
        """
        # 账号信息
        username = ''.join([random.choice(printable[:printable.index('!')]) for i in range(9)])
        password = ''.join([random.choice(printable[:printable.index(' ')]) for j in range(15)])
        email = username + email_class

        return username, password, email

    @staticmethod
    def generate_life_cycle(life_cycle: int):
        return str(datetime.now() + timedelta(days=life_cycle)).split('.')[0]

    def set_spiderOption(self, ):
        """浏览器初始化"""

        options = ChromeOptions()

        # 最高权限运行
        options.add_argument('--no-sandbox')

        # 隐身模式
        options.add_argument('-incognito')

        # 无缓存加载
        options.add_argument('--disk-cache-')

        # 静默启动
        if self.silence is True:
            options.add_argument('--headless')

        """自定义选项"""

        # 无反爬虫机制：高性能启动，禁止图片加载及js动画渲染，加快selenium页面切换效率
        def NonAnti():
            chrome_prefs = {"profile.default_content_settings": {"images": 2, 'javascript': 2},
                            "profile.managed_default_content_settings": {"images": 2}}
            options.experimental_options['prefs'] = chrome_prefs
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            d_c = DesiredCapabilities.CHROME
            d_c['pageLoadStrategy'] = 'none'

            return Chrome(
                options=options,
                executable_path=CHROMEDRIVER_PATH,
                desired_capabilities=d_c
            )

        if self.anti is False:
            return NonAnti()
        else:
            # 有反爬虫/默认：一般模式启动
            return Chrome(options=options, executable_path=CHROMEDRIVER_PATH)

    def sign_in(self, api: Chrome):
        """Please rewrite this function!"""

    def sign_up(self, api: Chrome):
        """Please rewrite this function!"""

    @staticmethod
    def wait(api: Chrome, timeout: float, tag_xpath_str):
        WebDriverWait(api, timeout).until(EC.presence_of_element_located((
            By.XPATH, tag_xpath_str
        )))

    def check_in(self, button_xpath_str: str):
        """daily check in ,add available flow"""

    def load_any_subscribe(self, api, element_xpath_str: str, href_xpath_str: str, class_: str):
        self.subscribe = WebDriverWait(api, 20).until(EC.presence_of_element_located((
            By.XPATH,
            element_xpath_str
        ))).get_attribute(href_xpath_str)

        save_login_info(self.subscribe, class_, self.life_cycle)

    def run(self):
        """Please rewrite this function!"""

        # Get register url

        # Locate register tag and send keys

        # Click the submit button

        # * Shut down the sAirPort TOS pop-us

        # * Jump to the login page
        # ** Locate sign in tag and send keys
        # ** Click the sign in button

        # To the sAirPort homepage

        # Wait for page elements to load

        # Get the subscribe link of ssr/trojan/v2ray

        # Save subscribe link and refresh redis task list

        # Close Chrome driver and release memory


if __name__ == '__main__':
    pass
