listMenu = [
    {
        "id": "1",
        "name": "开始",
    },
    {
        "id": "2",
        "name": "界面",
    },
    {
        "id": "3",
        "name": "设置",
    },
]

def get_menu():
    str_menu = ""
    str_menu = str_menu + "----------------------\n"
    for item in listMenu:
        str_menu = str_menu + f"{item['id']} - {item['name']}\n"
    str_menu = str_menu + "----------------------"
    return str_menu

def get_menu_from_index(index):
    str_menu = ""
    for item in listMenu:
        print(f"{item['id']} - {item['name']}\n")
        print(f"index: {index}\n")
        if int(item['id']) == index:
            str_menu = f"{item['name']}\n"
    return str_menu