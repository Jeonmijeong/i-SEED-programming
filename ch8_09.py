# 9. 문자열을 반대의 순서로 출력하는 코드입니다. 빈칸을 채우세요.
inStr, outStr = "Python", ""
strLen = len(inStr)

for i in range(0, strLen):
    outStr += inStr[-i-1]
print("내용을 거꾸로 출력 --> %s"%outStr)
