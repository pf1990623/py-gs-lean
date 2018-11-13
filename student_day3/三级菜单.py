china_map = {
    '山东': {
        '青岛': ['四方', '黄岛', '崂山', '李沧', '城阳'],
        '济南': ['历城', '槐荫', '高新', '长青', '章丘'],
        '烟台': ['龙口', '莱山', '牟平', '蓬莱', '招远']
    },
    '江苏': {
        '苏州': ['沧浪', '相城', '平江', '吴中', '昆山'],
        '南京': ['白下', '秦淮', '浦口', '栖霞', '江宁'],
        '无锡': ['崇安', '南长', '北塘', '锡山', '江阴']
    },
    '浙江': {
        '杭州': ['西湖', '江干', '下城', '上城', '滨江'],
        '宁波': ['海曙', '江东', '江北', '镇海', '余姚'],
        '温州': ['鹿城', '龙湾', '乐清', '瑞安', '永嘉']
    },
    '安徽': {
        '合肥': ['蜀山', '庐阳', '包河', '经开', '新站'],
        '芜湖': ['镜湖', '鸠江', '无为', '三山', '南陵'],
        '蚌埠': ['蚌山', '龙子湖', '淮上', '怀远', '固镇']
    },
    '广东': {
        '深圳': ['罗湖', '福田', '南山', '宝安', '布吉'],
        '广州': ['天河', '珠海', '越秀', '白云', '黄埔'],
        '东莞': ['莞城', '长安', '虎门', '万江', '大朗']
    }
}

while True:
    print("省份".center(50, '*'))
    for i in china_map.keys():
        print(i)
    sf = input("输入省份名称[退出q]:").strip()
    while True:
        if sf in china_map:
           print("市".center(50, '*'))
           for i in china_map.get(sf):
               print(i)
           city = input("输入城市名称[返回上一层b,退出q]:").strip()
           if city in china_map[sf].keys():
               print("区".center(50, '*'))
               while True:
                   for i in china_map[sf][city]:
                       print(i)
                   p_id = input("已经最后一层，[返回上一层b,退出q]").strip()
                   if p_id == "b":
                       break
                   elif p_id == 'q':
                       exit()
                   else:
                       print("输入错误")
           elif city == "b":
               break
           elif city == 'q':
               exit()
           else:
               print("您输入的城市不存在，请重新输入")
        elif sf == 'q':
           exit()
        else:
           print("您输入的省份不存在，请重新输入")

# 方法升级

current_level = menu
last_level = []
while True:
    for key in current_level:
        print(key)
    choice = input(">>:").strip()
    if choice == "b":
        if not last_level:break
        current_level = last_level[-1]
        last_level.pop()  # 把当前层改为父亲层，这样就返回上一层
    if choice == 'q': exit()
    if len(choice) == 0: continue
    if choice not in current_level:continue
    last_level.append(current_level)
    current_level = current_level[choice]  # 进入下一层

