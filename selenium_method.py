# chromedriver-mac-arm64_137.0.7151.119

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

import utils


def init_driver():
    global service
    global chrome_options
    if utils.get_os_from_platform() == "macOS" :
        service = Service("./resources/chromedriver_mac")
    elif utils.get_os_from_platform() == "Windows" :
        service = Service("./resources/chromedriver.exe")
    elif utils.get_os_from_platform() == "Linux" :
        service = Service("./resources/chromedriver_linux")

    # 1. 配置 Chrome 选项
    chrome_options = Options()

    # 2. 常见配置参数（可选）
    # 设置浏览器启动参数
    chrome_options.add_argument("--start-maximized")  # 最大化窗口
    chrome_options.add_argument("--disable-infobars")  # 禁用信息栏
    chrome_options.add_argument("--disable-extensions")  # 禁用扩展
    chrome_options.add_argument("--disable-gpu")  # 禁用 GPU 加速（某些系统需要）
    chrome_options.add_argument("--no-sandbox")  # 禁用沙盒模式（Docker 环境需要）
    chrome_options.add_argument("--disable-dev-shm-usage")  # 限制内存使用

    # 设置代理（示例）
    # chrome_options.add_argument('--proxy-server=http://127.0.0.1:8080')

    # 设置下载路径
    chrome_options.add_argument("--download-path=./resources/download")

    # 设置用户数据目录（保留登录状态）
    # chrome_options.add_argument("--user-data-dir=/path/to/user/data")

    # 禁用某些功能（如自动播放视频）
    chrome_options.add_argument("--disable-features=MediaRouter")

    # 处理证书错误（忽略SSL证书错误）
    chrome_options.add_argument("--ignore-certificate-errors")

    chrome_options.add_experimental_option("detach", True)

    # 3. 设置 ChromeDriver（推荐使用 WebDriver Manager 自动管理）
    # service = Service(ChromeDriverManager().install())

    # 4. 初始化浏览器
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    print("Initializing Chrome")
    print(f"service: {service}")


def login_in():
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # driver.implicitly_wait(10)

        # 5. 打开网页
        driver.get("https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&path=%2Faccount%2F&rv=1")

        # 6. 等待页面加载（示例）
        time.sleep(5)

        driver.refresh()

        # 实例化 By 类的对象
        by_xpath = By.XPATH

        # 7. 执行其他操作（示例）
        # weLoginBtn = driver.find_element("id", "s-top-loginbtn")
        # weLoginBtn.click()
        #
        # # TANGRAM__PSP_11__userName
        # # 等待最多10秒，直到div元素显示在页面上
        str_user_name = None
        input_user_name_element_wait = None

        str_user_name = input("user name: ")
        if str_user_name == "":
            import account_model
            str_user_name = account_model.user_name

        try:
            input_user_name_element_wait = WebDriverWait(driver, 20).until(
                # EC.presence_of_element_located((By.ID, "account_name_text_field"))
                EC.presence_of_element_located((By.XPATH, "//input[@id = 'account_name_text_field']"))
            )
            print("Div元素已显示！")

            input_user_name_element_wait.send_keys(f"{str_user_name}")
        except Exception as e:

            print("error ", e)
        finally:

            # input_user_name_element_wait.send_keys(f"{str_user_name}")
            print("加载用户名输入框完成")

        #
        # input_password_element_wait = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__password"))
        # )
        # str_password = input("password: ")
        # input_password_element_wait.send_keys(f"{str_password}")
        #
        # checkbox_agree_element_wait = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__isAgree"))
        # )
        # checkbox_agree_element_wait.click()
        #
        # login_btn_element_wait = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "TANGRAM__PSP_11__submit"))
        # )
        # driver.execute_script("arguments[0].click();", login_btn_element_wait)

        # search_box = driver.find_element("name", "q")
        # search_box.send_keys("Selenium Chrome配置")
        # search_box.submit()

        # 8. 等待搜索结果
        time.sleep(5)

    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        print("结束")
        # 9. 关闭浏览器
        # driver.quit()