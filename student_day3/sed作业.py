def fench(data):
    backend_data = "backend %s" %data
    record_list = []
    with open('haproxy.conf','r',encoding='utf-8') as f:
        tag = False
        for line in f:
            if line.strip() == backend_data:
                tag = True
                continue
            if tag and line.startswith('backend'):
                break
            if tag and line:
                record_list.append(line.strip())
        for line in record_list:
            print(line)
        return record_list

def add(data):
    backend = data['backend']
    record_list = fench(backend)
    current_record = "server %s %s weight %s maxconn %s" %(data['record']['server'],\
                                                           data['record']['server'],
                                                           data['record']['weight'],
                                                           data['record']['maxconn'])
    backend_data = "backend %s" % backend
    if not record_list:
        record_list.append(backend_data)
        record_list.append(current_record)
        with open('haproxy.conf', 'r', encoding="utf-8")as read_file,\
                open('haproxy_new.conf', 'w', encoding='utf-8') as new_file:
            for r_line in read_file:
                new_file.write(r_line)

            for new_line in record_list:
                if new_line.startswith("backend"):
                    new_file.write(new_line+'\n')
                else:
                    new_file.write("%s%s\n" % (' '*8, new_line))

def remove(data):
    pass

# {"backend":'www.oldboy1.com',"record":{'weight':22,"maxconn":33,'server':'1.1.1.1'}}
if __name__ == '__main__':
    msg = """
    1:查询
    2:添加
    3:删除
    4:退出
    
    """
    menu_dic = {
        '1': fench,
        '2': add,
        '3': remove,
        '4': exit,

    }
    # menu_dic['1']()

    while True:
        print(msg)
        choice = input("操作: ").strip()
        if len(choice) == 0 or choice not in menu_dic: continue
        if choice == '4': break

        data = input("数据>>: ").strip()
        if choice != '1':
            data = eval(data)

        # menu_dic[choice]函数名==fetch
        menu_dic[choice](data)