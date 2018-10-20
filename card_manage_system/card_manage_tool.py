"""
名片管理系统,有增,删,改,查功能
系统需求
程序启动，显示名片管理系统欢迎界面，并显示功能菜单
**************************************************
欢迎使用【名片管理系统】V1.0

1. 新建名片
2. 显示全部
3. 查询名片

0. 退出系统
**************************************************
用户用数字选择不同的功能
根据功能选择，执行不同的功能
用户名片需要记录用户的 姓名、电话、QQ、邮件
如果查询到指定的名片，用户可以选择 修改 或者 删除 名片
"""



cards = [{'name':'huping', 'phone':'11111111111', 'qq':'11', 'email':'11'}]
def welcome():
    """名片管理系统欢迎界面，并显示功能菜单"""
    print('*' * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print('1. 新建名片')
    print('2. 显示全部')
    print('3. 查询名片')
    print()
    print('0. 退出系统')
    print('*' * 50)


def add_card():
    """增加名片"""
    while True:
        card = {}
        card['name'] = input('enter your name:(6-20位): ')
        card['phone'] = input('enter your phone number:(11位): ')
        card['qq'] = input('enter your qq number: ')
        card['email'] = input('enter your email: ')
        if len(card['name']) in range(2, 21) and len(card['phone']) == 11:
            cards.append(card)
            print('新建成功!')
            break
        else:
            print('姓名长度或电话号码长度不符,请按要求输入.')


def show_cards():
    """显示全部名片"""
    print("姓名\t\t\t电话\t\t\t\tqq\t\t\t邮箱")
    print('-' * 70)
    for card in cards:
        # print("%s\t\t%s\t\t%s\t\t%s" % (card['name'], card['phone'], card['qq'], card['email']))
        for value in card.values():
            print(value, end='\t\t')
        print()


def find_card():
    """查询名片"""
    card_name = input("请输入要查询的名片姓名: ")
    for card in cards:
        if card['name'] == card_name:
            print('找到该名片')
            while True:
                choice = input("请输入对名片的操作: (1:修改, 2:删除, 0:返回上一级)  :  ")
                if choice == '0':
                    print('您选择返回上一级')
                    break
                elif choice == '2':
                    print('您选择删除查询到的名片')
                    cards.remove(card)
                    print('已删除, 删除的名片是%s:' % card)
                    break
                elif choice == '1':
                    print('您选择修改查询到的名片')
                    while True:
                        card['name'] = input('enter your name: ')
                        card['phone'] = input('enter your phone number: ')
                        card['qq'] = input('enter your qq number: ')
                        card['email'] = input('enter your email: ')
                        if len(card['name']) in range(6, 21) and len(card['phone']) == 11:
                            print('修改成功!')
                            break
                        else:
                            print('姓名长度或电话号码长度不符,请按要求输入.')
                    break
                else:
                    print('输入有误，请重新输入。')
            break

    else:
        print('没有找到该名片')


