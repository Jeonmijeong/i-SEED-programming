# 11. 입력된 문자열 중에서 한글과 영문자만 남기는 프로그램을 작성하세요.
input = "파이썬###CookBook$$$@@@열공중1234"
output = ''
for i in input:
    if '가' <= i <= '힣' or 'A' <= i <= 'Z' or 'a' <= i <= 'z':
        output += i
print(output)
