#   10、写代码，完成下列需求：
#       用户可持续输入（用while循环），用户使用的情况：
#       输入A，则显示走大路回家，然后在让用户进一步选择：
#           是选择公交车，还是步行？
#           选择公交车，显示10分钟到家，并退出整个程序。
#           选择步行，显示20分钟到家，并退出整个程序。
#       输入B，则显示走小路回家，并退出整个程序。
#       输入C，则显示绕道回家，然后在让用户进一步选择：
#           是选择游戏厅玩会，还是网吧？
#           选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B, C选项。
#           选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B, C选项。

while True:
    print("输入A or B or C")
    chiose = input('>>>')
    if chiose == 'A':
        print("1.公交车，2.步行？")
        chiose_A = input(">>>")
        if chiose_A == 1:
            print("10分钟到家")
            break
        else:
            print("20分钟到家")
            break
    elif chiose == 'B':
        print("走小路回家")
        break
    elif chiose == 'C':
        print("1.游戏厅，2、网吧")
        chiose_C = input(">>>")
        if chiose_C == 1:
            print("一个半小时到家，爸爸在家，拿棍等你")
            continue
        else:
            print("两个小时到家，妈妈已做好了战斗准备。")
            continue
