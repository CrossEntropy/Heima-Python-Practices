#! /usr/bin/python3
# 程序的功能函数在这文件里

# 记录所有的名片字典的列表
card_list = [{"姓名": "张三",
              "电话": "110",
              "QQ": "123",
              "邮箱": "zs@itheima.com"},
             {"姓名": "李四",
              "电话": "120",
              "QQ": "178",
              "邮箱": "ls@itheima.com"},
             ]
# 记录字典的键
card_keys = ["姓名", "电话", "QQ", "邮箱"]


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
    card_dict = {"姓名": name_str, "电话": phone_str,
                 "QQ": qq_str, "邮箱": email_str}
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


def show_card(card_dict):
    """显示出输入名片字典的信息

    :param card_dict: 名片字典
    :return: 空
    """
    # 打印表头
    for key in card_keys:
        print(key, end="\t\t")
    # 换行
    print("")
    # 打印分隔符
    print("=" * 40)
    # 打印名片信息
    for key in card_keys:
        print(card_dict[key], end="\t\t")
    # 换行
    print("")


def judge_input(tip_message, card_value):
    """判断用户输入的信息.

    判断用户输入的信息, 如果用户输入信息是回车, 则不改变名片的值.
    :param tip_message:
        input函数的提示信息.
    :param card_value:
        名片字典的值.
    :return:
        如果 tip_message 为回车, 则返回card_value.
        如果 tip_message 不为回车, 则返回用户的输入值

    """
    input_str = input(tip_message)
    if len(input_str) == 0:
        return card_value
    return input_str


def modify_card(card_dict):
    # 提示用户输入信息
    name_str = judge_input("请输入姓名[回车不修改]： ", card_dict["姓名"])
    phone_str = judge_input("请输入电话号码[回车不修改]： ", card_dict["电话"])
    qq_str = judge_input("请输入QQ[回车不修改]: ", card_dict["QQ"])
    email_str = judge_input("请输入邮箱[回车不修改]: ", card_dict["邮箱"])
    information = [name_str, phone_str, qq_str, email_str]
    # 修改当前名片的信息
    for index, key in enumerate(card_keys):
        card_dict[key] = information[index]
    print("修改完成")
    # 打印出修改好的信息


def search_card():
    """查找用户信息."""
    # 1. 提示用户输入要搜索的姓名
    name_str = input("请输入要搜索的姓名： ")
    # 2. 遍历名片列表, 查询姓名, 如果没有找到, 需要提示用户
    for card_dict in card_list:  # 遍历名片列表
        # 姓名不相符, 退出本次循环
        if card_dict["姓名"] != name_str:
            continue
        # 3. 姓名找到, 打印出名片信息
        show_card(card_dict)
        # 4. 提示用户的输入下一步操作：
        #    0---返回上一级  1---修改名片 2---删除名片
        #    修改名片之后, 再次提示
        #    删除名片之后, 返回到功能菜单
        while True:
            print("请选择您的操作----> ")
            print("0. 返回上一级, 1. 修改该名片, 2. 删除该名片")
            user_option = input("请输入您的操作： ")
            if user_option == "0":  # 为0, 返回到功能菜单
                return  # 结束函数
            elif user_option == "1":  # 为1, 进行名片的修改
                # 修改名片
                modify_card(card_dict)
                # 显示修改好的名片
                show_card(card_dict)
            elif user_option == "2":  # 为2, 删除该名片
                card_list.remove(card_dict)
                print("删除%s的名片成功"%name_str)
                return  # 结束函数
            else:  # 输入信息不正确, 提示用户重新输入
                print("您的输入信息不正确！请重新输入.")
    else:  # 全部迭代完, 没有搜寻到指定的姓名, 提示用户, 并返回功能菜单
        print("没有找到您输入姓名的名片！将返回到功能菜单.")


if __name__ == "__main__":
    new_card()