print("猜一个数字游戏")
num = input("请猜一个数字：")
guss = int(num)
if guss == 8:
    print("你猜对了！")
    print("不过，猜对了也没有奖励哦")
elif guss == 6:
    print("你猜对了！")
else:
    print("你猜错啦！")