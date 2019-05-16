#! /usr/bin/python3
# 程序的入口
# 每一次启动名片管理系统都通过main这个文件启动
import card_tool


while True:  # 进行一个无限循环,由用户决定什么时候退出循环

    # 显示功能菜单
    card_tool.show_menu()

    # 用户输入
    action_str = input("请选择希望执行的操作： ")
    print("您选择的操作是【%s】"%action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 输入为1进行新增名片的操作
        if action_str == "1":
            card_tool.new_card()
        # 输入为2进行显示全部的操作
        elif action_str == "2":
            card_tool.show_all_card()
        # 输入为3进行查询名片的操作
        else:
            card_tool.search_card()
        pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("您的输入错误, 请输入数字1, 2, 3其中的一个")