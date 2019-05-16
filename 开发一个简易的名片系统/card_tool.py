# 程序的功能函数在这文件里

# 记录所有的名片字典
card_list = [{"姓名": "张三",
              "电话": "110",
              "QQ": "123",
              "邮箱": "zs@itheima.com"},
             {"姓名": "李四",
              "电话": "120",
              "QQ": "178",
              "邮箱": "ls@itheima.com"},
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
    # 打印分割线
    print("-" * 40)
    print("-" * 40)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名： ")
    phone_str = input("请输入电话号码： ")
    qq_str = input("请输入QQ: ")
    email_str = input("请输入邮箱: ")

    # 2. 使用用户输入的信息建立一个名片的字典
    card_dict = {"姓名": name_str,
              "电话": phone_str,
              "QQ": qq_str,
              "邮箱": email_str}
    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)

    # 4. 提示用户添加成功
    print("添加成功")
    print("=" * 40)


def show_all_card():
    """显示所有名片"""
    # card_list为空
    if len(card_list) == 0:
        print("=" * 40)
        print("当前名片中没有任何用户信息！！！请添加！！！")
        print("=" * 40)
        return None

    # card_list不为空
    print("显示全部名片")
    # 打印表头
    card_keys = ["姓名","电话", "QQ", "邮箱"]
    for i in card_keys:
        print(i, end="\t\t")
    print("")
    # 打印分割线
    print("="*40)
    # 遍历名片列表依次输出字典信息
    for card_dict in card_list:
        # 遍历字典的键, 输出值的信息
        for key in card_keys:
            print(card_dict[key], end="\t\t")
        # 换行
        print("")


def search_card(name):
    """寻找用户信息"""

    print("*" * 40)
    print("搜索名片")


if __name__ == "__main__":
    new_card()