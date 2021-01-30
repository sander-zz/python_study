x = int(input('x='))
y = int(input('y='))
if(y < x):
    x, y = y, x
# 从两个数中较小的数开始做递减的循环
for factory in range(x, 0, -1):
    if(x % factory == 0 and y % factory == 0):
        print('%d和%d的最大公约数是%d' % (x, y, factory))
        print('%d和%d的最小公倍数为%d' % (x, y, x * y//factory))
        break



