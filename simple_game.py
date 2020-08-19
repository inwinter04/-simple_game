#无聊写的程序

###导入模块-开始###
import random #导入生成随机数模块
import easygui as gui #导入用户界面模块
import os #导入系统操作模块（施工中。。。）
import pickle #导入高大上的咸菜！（施工中。。。）
###导入模块-结束###

###初始化-开始###
me_url = os.curdir + 'points.me'
if me_url == False:
    points = open("points.me",mode="wb")
    pickle.dump(0,me_url)
    points.close
gui.msgbox(msg="这是一个猜数字的小游戏！",title="猜数字小游戏",ok_button="开始游戏") #进入程序后的欢迎语
###初始化-结束###

###函数-开始###
def model_choice(): #定义一个函数
    global model #声明一个全局变量
    model = gui.buttonbox(msg="""——————模式大全——————
[1]简单（范围1-5随机整数）
[2]普通（范围1-10随机整数）
[3]魔鬼模式（范围1-5随机实数。可以尝试50次！）
[4]自定义模式（随机数范围自定义。尝试次数自定义）
[0]开发中...
——————模式大全——————
请选择您的模式！
""",title="猜数字小游戏",choices=("简单","普通","魔鬼","自定义")) #用户返回一个模式(字符串)
    global model_continue #声明一个全局函数
    model_continue = "不了不了" #将变量赋值

def model_points():
    points = open(me_url,mode="wb")
    num_points = pickle.load(me_url)
    if model == "简单":
        pass
    elif model == "普通":
        if time <= 2:
            num_points += 5
            pickle.dump(num_points,me_url)
        elif time <= 5 and time > 2:
            num_points += 2
            pickle.dump(num_points,me_url)
        elif time <= 8 and time > 5:
            pass
    elif model == "魔鬼":
        if time <= 10:
            num_points += 50
            pickle.dump(num_points,me_url)
        elif time <= 30 and time > 10:
            num_points += 20
            pickle.dump(num_points,me_url)
        elif time <= 50 and time > 30:
            num_points += 10
            pickle.dump(num_points,me_url)
    points.close



#下面是主程序的函数（下面四个模式全部依赖于此函数）
def main_model(num_start,num_stop,max_time,type_same,type_int):#num_start最小数 num_stop最大数 max_time最大次数 type_same数据类型 type_int是否为整型
    global model_continue #声明一个全局函数
    global time
    model_continue = "继续游戏" #声明一个变量来确定程序是否应该继续运行
    while model_continue == "继续游戏": #如果状态为继续游戏就一直循环
        time = 1 #初始化次数
        right = int(random.randint(num_start,num_stop)) if type_int == "yes" else random.uniform(num_start,num_stop) #使用random模块初始化出一个数字，该数字赋值为【right】变量(根据模式的不同而生成不同的数字类型。)
        guess = gui.integerbox(msg="猜猜我心里面想的数字：",title="猜数字小游戏",lowerbound=0,upperbound=100) if type_int == "yes" else float(gui.integerbox(msg="猜猜我心里面想的数字：",title="猜数字小游戏",lowerbound=0,upperbound=100)) #要求用户返回一个值。并将其值赋值为【guess】变量
        if guess == right: #判断猜想与正确答案是否相同
            gui.msgbox(msg="太厉害了！你尽然第一次就答对了！不过答对了也没有奖励的哦！",title="猜数字小游戏",ok_button="太棒了！") #若第一次就相同，则输出一个信息框告诉用户回答正确。
        else: #下面为第一次猜想与正确答案不相同所执行的操作
            while ( time <= max_time ) and ( guess != right ): #若后面的猜想不正确，且次数还没有达到最大次数，则进行循环
                guess = type_same(gui.enterbox(msg="不对哦，答案不是"+str(guess)+"您还有"+str(max_time - time)+"次机会！"+"再悄悄告诉你：你的数字太小了~" if guess < right else "再悄悄告诉你：你的数字太大了~"+"再尝试一下：",title="猜数字小游戏")) #使用三元操作符判断用户的猜想与正确答案的大小关系。并返回给用户，要求用户重新输入猜想
                time += 1 #次数增加一次。当超过最大次数的时候，则无法继续此循环。
            gui.msgbox(msg="恭喜你，终于答对了！正确答案就是："+str(right)+"\n你尽然只用了"+str(time)+"次就答对了！\n真是不可思议！",title="猜数字小游戏",ok_button="太棒了！") if guess == right else gui.msgbox(msg="哎呀，都答错了！正确答案是：" + str(right),title="猜数字小游戏",ok_button="好吧！") #使用三元操作符判断用户是因为达到最大次数而跳出循环还是因为后面答对了跳出循环。两种情况给出不同的信息框
        #model_points()
        model_continue = gui.buttonbox(msg="请选择...",title="猜数字小游戏",choices=("继续游戏","切换模式","不了不了")) #在游戏结束后，要求用户选择是否继续游戏，或者切换其他模式
###函数-结束###

###主程序运行-开始###
try: #检查语句
    model_continue = "切换模式" #初始化的变量值，使程序开始进行
    while model_continue == "切换模式": #主循环体
        model_choice() #调用询问用户模式函数。返回一个值(字符串)

        ###模式一-开始###
        if model == "简单": #若用户选择的模式为简单。则执行以下语句
            main_model(1,5,5,int,"yes") #简单模式下，猜想最小次数为1。猜想最大次数为5。正确答案最大数为5。用户输入的值将会转为整型。
        ###模式一-结束###

        ###模式二-开始###
        elif model == "普通": #若用户选择的模式为普通。则执行以下语句
            main_model(1,10,5,int,"yes") #普通模式下，猜想最小次数为1。猜想最大次数为10。正确答案最大数为5。用户输入的值将会转为整型。
        ###模式二-结束###

        ###模式三-开始###
        elif model == "魔鬼": #若用户选择的模式为魔鬼。则执行以下语句
            gui.msgbox(msg="进入魔鬼模式！如果在这个模式下轻松通过，可以直接去买彩票！",title="猜数字小游戏",ok_button="知道啦！") #魔鬼模式下特殊的提示语
            main_model(1,5,50,float,"no") #魔鬼模式下，猜想最小次数为1。猜想最大次数为5。正确答案最大数为50。用户输入的值将会转为浮点型。
        ###模式三-结束###

        ###模式四-开始###
        elif model == "自定义": #若用户选择的模式为自定义。则执行以下语句
            ###本句存在未知问题###
            type_same = int if gui.ccbox(msg='是否开启魔鬼模式？', title='猜数字小游戏', choices=["是","否"]) == "否" else float #询问用户是否开启魔鬼模式。若用户选择“是”，则给【type_same】赋值为int。反之，将其赋值为float
            ###本句存在未知问题###
            type_int = "no" if type_same == float else "yes" #跟随【type_same】同步。若其为“是”则【type_int】赋值为"no"。反之，赋值为"yes"
            num_start = float(gui.enterbox(msg='请输入随机数的范围的最小值（请输入一个数字）:', title='猜数字小游戏', default='1')) #询问用户正确答案的最小值（默认为1）
            num_stop = float(gui.enterbox(msg='请输入随机数的范围的最大值（请输入一个数字）:', title='猜数字小游戏', default='5')) #询问用户正确答案的最大值（默认为5）
            max_time = int(gui.enterbox(msg='请输入游戏可以尝试的最大次数（请输入一个数字）：', title='猜数字小游戏', default='5')) #询问用户可以尝试的最大次数（默认为5）
            main_model(num_start,num_stop,max_time,type_same,type_int) #运行函数
        ###模式四-结束###

except (ValueError,TypeError): #错误检查。此处防止用户因输入不合法字符导致程序崩溃
    gui.msgbox(msg="鱼肠！\n出现错误！请重新开始！\n",title="猜数字小游戏",ok_button="emmmmm") #若出现不合法的值，立即拦截。且抛出错误告诉用户
###主程序运行-结束###

###游戏结束语-开始###
gui.msgbox(msg="欢迎下次再来玩哦~",title="猜数字小游戏",ok_button="知道啦！") #防止程序运行结束后自动关闭
###游戏结束语-结束###