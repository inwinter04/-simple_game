#无聊写的程序

###导入模块-开始###
import random
###导入模块-结束###

###次数变量-开始###
time = 1
###次数变量-结束###

###开始语-开始###
print ("这是一个猜数字的小游戏！\n您有五次回答机会哦！")
###开始语-结束###

###模式选择-开始###
model = int(input ("""模式选择————
                  [1]简单（范围1-5随机整数）
                  [2]普通（范围1-10随机整数）
                  [3]魔鬼模式（范围1-5随机实数。可以尝试50次！）
                  [4]待开发
                """)
            )
###模式选择-结束###

###模式一-开始###
if model == 1:
    right = int(random.randint(1,5))
    guess = int(input ("猜猜我心里面想的数字："))
    if guess == right:
        print("太厉害了！你尽然第一次就答对了！不过答对了也没有奖励的哦！")
    else:
        while  ( time <= 5 ) and ( guess != right ):
            times = str(time)
            times1 = 5-time
            print_times = str(times1)
            print_guess = str(guess)
            print ("不对哦，答案不是"+print_guess+"\n您还有"+print_times+"次机会！")
            if guess < right:
                print ("再悄悄告诉你：你的数字太小了~")
            else:
                print ("再悄悄告诉你：你的数字太大了~")
            guess = int(input ("再尝试一下:"))
            time += 1
        print_right = str(right)
        if guess == right:
            times = str(time)
            print ("恭喜你，终于答对了！正确答案就是："+print_right+"\n你尽然只用了"+times+"次就答对了！\n真是不可思议！")
        else:
            print ("哎呀，都答错了！正确答案是：" + print_right)
###模式一-结束###

###模式二-开始###
elif model == 2:
    right = int(random.randint(1,10))
    guess = int(input ("猜猜我心里面想的数字："))
    if guess == right:
        print("太厉害了！你尽然第一次就答对了！不过答对了也没有奖励的哦！")
    else:
        while  ( time <= 5 ) and ( guess != right ):
            times = str(time)
            times1 = 5-time
            print_times = str(times1)
            print_guess = str(guess) 
            print ("不对哦，答案不是"+print_guess+"\n您还有"+print_times+"次机会！")
            if guess < right:
                print ("再悄悄告诉你：你的数字太小了~")
            else:
                print ("再悄悄告诉你：你的数字太大了~")
            guess = int(input ("再尝试一下:"))
            time += 1
        print_right = str(right)
        if guess == right:
            times = str(time)
            print ("恭喜你，终于答对了！正确答案就是："+print_right+"\n你尽然只用了"+times+"次就答对了！\n真是不可思议！")
        else:
            print ("哎呀，都答错了！正确答案是：" + print_right)
###模式二-结束###

###模式三-开始###
elif model == 3:
    right = random.uniform(1,5)
    print ("进入魔鬼模式！如果猜中了，请直接出门买彩票！")
    guess = float(input ("猜猜我心里面想的数字："))
    if guess == right:
        print("太厉害了！你尽然第一次就答对了！不过答对了也没有奖励的哦！")
    else:
        while  ( time <= 50 ) and ( guess != right ):
            times = str(time)
            times1 = 50-time
            print_times = str(times1)
            print_guess = str(guess) 
            print ("不对哦，答案不是"+print_guess+"\n您还有"+print_times+"次机会！")
            if guess < right:
                print ("再悄悄告诉你：你的数字太小了~")
            else:
                print ("再悄悄告诉你：你的数字太大了~")
            guess = float(input ("再尝试一下:"))
            time += 1
        print_right = str(right)
        if guess == right:
            times = str(time)
            print ("恭喜你，终于答对了！正确答案就是："+print_right+"\n你尽然只用了"+times+"次就答对了！\n真是不可思议！")
        else:
            print ("哎呀，都答错了！正确答案是：" + print_right)
###模式三-结束###

###模式四-开始###
elif model == 4:
    print ("开发中...")
###模式四-结束###

###模式选择错误-开始###
elif model != 1 or 2 or 3 or 4:
    print ("还没有这个模式呢！")
###模式选择错误-结束###

###防止程序运行结束后自动关闭###
input ("GAME OVER!\n按下任何按键均可退出程序！")
###防止程序运行结束后自动关闭###