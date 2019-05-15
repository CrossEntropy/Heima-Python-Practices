# 程序的功能函数在这文件里

# 记录所有的名片字典
card_list = [{"姓名": "张三",
              "电话": 110,
              "qq": 12345,
              "email": "zs@itheima.com"},
             {"姓名": "李四",
              "电话": 120,
              "qq": 17845,
              "email": "ls@itheima.com"},
             ]


def show_menu():
    """显示功能菜单."""
    print("*" * 40)
    print("欢迎使用【名片管理系统】v1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 40)


def new_card():
    """添加名片信息. """
    print("*" * 40)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name = input("请输入姓名： ")
    phone = input("请输入电话号码： ")
    qq = input("请输入QQ: ")
    email = input("请输入email: ")

    # 2. 使用用户输入的信息建立一个名片的字典
    card_dict = {"姓名": name,
              "电话": phone,
              "qq": qq,
              "email": email}
    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)
    
    # 4. 提示用户添加成功
    print("添加成功")
    print("*" * 40)


def show_all_card():
    """"""
    print("*" * 40)
    print("显示所有名片")


def search_card():
    """"""
    print("*" * 40)
    print("搜索名片")


if __name__ == "__main__":
    show_menu()