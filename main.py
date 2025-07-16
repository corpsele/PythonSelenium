
import sys

import app_main
import menu
import selenium_method
import utils


class Main:
    def __init__(self):
        print("main")
        selenium_method.init_driver()
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




if __name__ == "__main__":
    main = Main()
