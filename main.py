
import sys

import app_main
import menu
import selenium_method
import utils
import account_model


class Main:
    def __init__(self):
        print("main")
        selenium_method.init_driver()
        self.read_config()
        self.init_config()

    def init_config(self):
        print("init config")
        print(f"os = {utils.get_os_from_platform()}, os = {utils.get_os_from_os()}")
        print(menu.get_menu())
        choice = input("请选择：")
        str_choice = menu.get_menu_from_index(int(choice))
        print("已经选择", str_choice)
        match choice:
            case "1":
                print(1)
                selenium_method.login_in()
            case "2":
                print(2)
                app_main.show_root()
            case "3":
                print(3)

    def read_config(self):
        print("read config")
        data = utils.read_json_file("./resources/config.json")
        url = data.get("url")
        apple_accounts = data.get("apple_accounts")
        apple_account = apple_accounts[0]
        account_model.user_name =  apple_account.get("user_name")
        account_model.password = apple_account.get("password")
        print(data)
        print(url)
        print(apple_account)
        print(account_model.user_name)
        print(account_model.password)


if __name__ == "__main__":
    main = Main()
