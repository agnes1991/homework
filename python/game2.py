#coding:utf-8
print("猜一个数字游戏")
num = input("请猜一个数字：")
answer = 6
guss = int(num)

while True:
    if guss == answer:
        break
    # num = input("请继续猜一个数字：")
    # guss = int(num)
    guss = int(input("请继续猜一个数字："))


print("猜对了！")