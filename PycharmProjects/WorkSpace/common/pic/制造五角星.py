import turtle
from turtle import *

# # 设置笔刷宽度:
# width(5)
# # 前进:
# forward(100)
# # 右转90度:
# right(45)
# # 笔刷颜色:
# pencolor('red')
width(5)
for i in range(5):
    if (i % 2) == 0:
        pencolor('red')
    else:
        pencolor('green')
    turtle.forward(100)
    turtle.right(144)
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()