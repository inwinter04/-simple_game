"""
2020.12.22
通过比较输入的站数，给出所需要支付的价格，并且输出。
小于等于5站，需要2块钱
大于5站小于等于10站，需要3块钱
大于10站小于等于16站，需要4块钱
大于16站，需要5块钱
"""
import easygui as gui
global num
def main(mon):
    gui.msgbox(msg="乘坐"+str(num)+"站需要："+str(mon)+"元！",title="深圳通+",ok_button="了解！")
online = "在线"
while online == "在线":
    try:
        num = int(gui.enterbox(msg="请输入您所需要乘坐的站数：",title="深圳通+",default="这里只可以输入数字哦~~~~"))
    except:
        gui.msgbox(msg="鱼肠！请认您输入的是一个合法的数字！")
    if num <= 5:
        main(2)
    elif num <= 10 and num > 5:
        main(3)
    elif num <= 16 and num > 10:
        main(4)
    elif num > 16:
        main(5)
    choice = gui.ccbox(msg="是否继续该程序？",title="深圳通+",choices=("继续","结束"),default_choice="继续",cancel_choice="结束")
    if choice == "结束":
        online = "离线"
gui.msgbox(msg="已退出程序，欢迎下次使用QWQ",title="深圳通+",ok_button="了解！")
