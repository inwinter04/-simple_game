#无聊写的程序

###导入模块-开始###
import random
import easygui as gui
###导入模块-结束###

###开始语-开始###
gui.msgbox(msg="这是一个猜数字的小游戏！",title="猜数字小游戏",ok_button="开始游戏")
###开始语-结束###

###模式选择-开始###
model = gui.buttonbox(msg="""——————模式大全——————
[1]简单（范围1-5随机整数）
[2]普通（范围1-10随机整数）
[3]魔鬼模式（范围1-5随机实数。可以尝试50次！）
[4]自定义模式（随机数范围自定义。尝试次数自定义）
[0]开发中...
——————模式大全——————
请选择您的模式！
""",title="猜数字小游戏",choices=("简单","普通","魔鬼","自定义"))
###模式选择-结束###

###函数-开始###
def main_model(num_start,num_stop,max_time,type_same,type_int):#num_start最小数 num_stop最大数 max_time最大次数 type_same数据类型 type_int整型
    time = 1
    right = int(random.randint(num_start,num_stop)) if type_int == "yes" else random.uniform(num_start,num_stop)
    guess = gui.integerbox(msg="猜猜我心里面想的数字：",title="猜数字小游戏",lowerbound=0,upperbound=100) if type_int == "yes" else float(gui.integerbox(msg="猜猜我心里面想的数字：",title="猜数字小游戏",lowerbound=0,upperbound=100))
    if guess == right:
        gui.msgbox(msg="太厉害了！你尽然第一次就答对了！不过答对了也没有奖励的哦！",title="猜数字小游戏",ok_button="太棒了！")
    else:
        while ( time <= max_time ) and ( guess != right ):
            guess = type_same(gui.enterbox(msg="不对哦，答案不是"+str(guess)+"您还有"+str(max_time - time)+"次机会！"+"再悄悄告诉你：你的数字太小了~" if guess < right else "再悄悄告诉你：你的数字太大了~"+"再尝试一下：",title="猜数字小游戏"))
            time += 1
        gui.msgbox(msg="恭喜你，终于答对了！正确答案就是："+str(right)+"\n你尽然只用了"+str(time)+"次就答对了！\n真是不可思议！",title="猜数字小游戏",ok_button="太棒了！") if guess == right else gui.msgbox(msg="哎呀，都答错了！正确答案是：" + str(right),title="猜数字小游戏",ok_button="好吧！")
###函数-结束###

try:
    ###模式一-开始###
    if model == "简单":
        main_model(1,5,5,int,"yes")
    ###模式一-结束###

    ###模式二-开始###
    elif model == "普通":
        main_model(1,10,5,int,"yes")

    ###模式二-结束###

    ###模式三-开始###
    elif model == "魔鬼":
        gui.msgbox(msg="进入魔鬼模式！如果在这个模式下轻松通过，可以直接去买彩票！",title="猜数字小游戏",ok_button="知道啦！")
        main_model(1,5,50,float,"no")
    ###模式三-结束###

    ###模式四-开始###
    elif model == "自定义":
        type_same = int if gui.ccbox(msg='是否开启魔鬼模式？', title='猜数字小游戏', choices=["是","否"]) == "否" else float  ###本句存在未知问题
        type_int = "no" if type_same == float else "yes"
        num_start = float(gui.enterbox(msg='请输入随机数的范围的最小值（请输入一个数字）:', title='猜数字小游戏', default='1', strip=True, image=None, root=None))
        num_stop = float(gui.enterbox(msg='请输入随机数的范围的最大值（请输入一个数字）:', title='猜数字小游戏', default='5', strip=True, image=None, root=None))
        max_time = int(gui.enterbox(msg='请输入游戏可以尝试的最大次数（请输入一个数字）：', title='猜数字小游戏', default='5', strip=True, image=None, root=None))
        main_model(num_start,num_stop,max_time,type_same,type_int)
    ###模式四-结束###

except (ValueError,TypeError):
    gui.msgbox(msg="鱼肠！\n出现错误！请重新开始！\n",title="猜数字小游戏",ok_button="emmmmm")

###防止程序运行结束后自动关闭###
gui.msgbox(msg="欢迎下次再来玩哦~",title="猜数字小游戏",ok_button="知道啦！")
###防止程序运行结束后自动关闭###