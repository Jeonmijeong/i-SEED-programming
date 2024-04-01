# 5. 문자열의 중간마다 $를 끼워 넣는 코드입니다. 빈칸을 채우세요.
ss = 'Python'

for i in range(len(ss)):
    if i != len(ss)-1:
        print(ss[i]+'$', end='')
    else:
        print(ss[i], end='')
