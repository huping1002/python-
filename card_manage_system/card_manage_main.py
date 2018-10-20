import card_manage_tool


while True:
    card_manage_tool.welcome()
    action = input('请选择操作功能: ')
    print("您选择的操作是:%s" % action)
    if action == '1':
        print('功能是: 新建名片')
        card_manage_tool.add_card()
    elif action == "2":
        print('功能是: 显示名片')
        card_manage_tool.show_cards()
    elif action == '3':
        print("功能是: 查询名片, 修改和删除")
        card_manage_tool.find_card()
    elif action == '0':
        print('您选择退出系统')
        print('已退出系统.')
        break
    else:
        print('输入错误, 请按照要求输入.')


