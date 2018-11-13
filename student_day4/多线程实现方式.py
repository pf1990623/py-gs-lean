import time
def consumer(name):
    print("%s 准备吃包子！" % name)
    while True:
        baozi = yield
        print("包子[%s]来了，被[%s]吃了" %(baozi,name))

def producer(name):
    c = consumer("A")
    c2 = consumer("B")
    c.__next__()
    c2.__next__()
    for i in range(10):
        time.sleep(1)
        print("做了两个包子")
        """
        #send和next方法基本一致，__next__()不支持传递参数，但是可以唤醒yield
        # send方法支持传递参数
        """
        c.send(i)
        c2.send(i)

producer("xiaofeng")