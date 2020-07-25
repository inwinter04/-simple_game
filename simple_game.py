#无聊写的程序

###导入模块-开始###
import random
###导入模块-结束###

###开始语-开始###
print ("这是一个猜数字的小游戏！")
###开始语-结束###

###模式选择-开始###
try:
    model = int(input ("""——————模式大全——————
[1]简单（范围1-5随机整数）
[2]普通（范围1-10随机整数）
[3]魔鬼模式（范围1-5随机实数。可以尝试50次！）
[4]自定义模式（随机数范围自定义。尝试次数自定义）
[0]开发中...
——————模式大全——————
请输入模式编号："""))
except (ValueError):
    print ("鱼肠，请输入一个合法数字！")
    input ("按下任何按键均可退出程序！")
###模式选择-结束###

###函数-开始###
def main_model(num_start,num_stop,max_time,type_same,type_int):#num_start最小数 num_stop最大数 max_time最大次数 type_same数据类型 type_int整型
    time = 1
    right = int(random.randint(num_start,num_stop)) if type_int == "yes" else random.uniform(num_start,num_stop)
    guess = type_same(input ("猜猜我心里面想的数字："))
    if guess == right:
        print("太厉害了！你尽然第一次就答对了！不过答对了也没有奖励的哦！")
    else:
        while  ( time <= max_time ) and ( guess != right ):
            print_str = "再悄悄告诉你：你的数字太小了~" if guess < right else "再悄悄告诉你：你的数字太大了~"
            print ("不对哦，答案不是"+str(guess)+"。您还有"+ str(max_time - time)+"次机会！" + print_str)
            guess = type_same(input ("再尝试一下:"))
            time += 1
        print ("恭喜你，终于答对了！正确答案就是："+str(right)+"\n你尽然只用了"+str(time)+"次就答对了！\n真是不可思议！") if guess == right else print ("哎呀，都答错了！正确答案是：" + str(right))
###函数-结束###

try:
    ###模式一-开始###
    if model == 1:
        main_model(1,5,5,int,"yes")
    ###模式一-结束###

    ###模式二-开始###
    elif model == 2:
        main_model(1,10,5,int,"yes")

    ###模式二-结束###

    ###模式三-开始###
    elif model == 3:
        print ("进入魔鬼模式！如果在这个模式下轻松通过，可以直接去买彩票！")
        main_model(1,5,50,float,"no")
    ###模式三-结束###

    ###模式四-开始###
    elif model == 4:
        type_same = float if str(input("是否开启魔鬼模式（请输入是/否）：")) == "是" else int
        type_int = "no" if type_same == float else "yes"
        num_start = float(input("随机数的范围的最小值（请输入一个数字）："))
        num_stop = float(input("随机数的范围的最大值（请输入一个数字）："))
        max_time = int(input("请输入游戏可以尝试的最大次数（请输入一个数字）："))
        main_model(num_start,num_stop,max_time,type_same,type_int)
    ###模式四-结束###

    ###模式零-开始###
    elif model == 0:
        print ("开发中...")
    ###模式零-结束###

    ###模式选择错误-开始###
    elif model != 0 or 1 or 2 or 3 or 4:
        print ("还没有这个模式呢！")
    ###模式选择错误-结束###
except (ValueError):
    print ("鱼肠，程序出现错误！")
    input ("按下任何按键均可退出程序！")

###防止程序运行结束后自动关闭###
input ("GAME OVER!\n按下任何按键均可退出程序！")
###防止程序运行结束后自动关闭###