# 11. 1부터 100까지의 합계(=5050)을 구하는 재귀 함수를 사용한 코드입니다. 재귀 함수의 빈칸을 완성하세요.
def addNumber(num):
    if num <= 1:
        return num
    else:
        return num + addNumber(num - 1)

print(addNumber(100))
