# 13. [프로그램1]를 변경해서 다음과 같이 글자가 나선형으로 안쪽으로 써지도록 코딩해보세요.
import turtle
import math
inStr = input("나 보기가 역겨워 가실 때에는 말없이 고이 보내 드리오리다 영변에 약산 진달래꽃 아름 따다 가실길에 뿌리오리다")
count = len(inStr)

wn = turtle.Screen()
wn.setup(width=500, height=500)

pen = turtle.Turtle()
pen.speed(0)

radius = 200
font_size = 20

total_angle = 360 * 2
angle_interval = total_angle / count

pen.penup()
pen.goto(0, -radius)
pen.pendown()

for i in range(count):
    char = inStr[i]
    angle = i * angle_interval
    
    radian = math.radians(angle)
    
    x = radius * math.cos(radian)
    y = radius * math.sin(radian)
    
    pen.penup()
    pen.goto(x, y)
    pen.setheading(-angle + 90)
    pen.pendown()
    
    pen.write(char, align="center", font=("Arial", font_size, "normal"))

wn.mainloop()
