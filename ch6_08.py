# 8. 다음은 for 문을 사용해서 1234부터 4567까지 444의 배수의 합계를 구하는 코드입니다. while 문으로 변경해서 코드를 다시 작성하세요.

# hap = 0
# for n in range(1234, 4568) :
#     if n % 444 == 0 :
#         hap += n

# print(hap)

hap = 0
n = 1234

while n <= 4567:
    if n % 444 == 0:
        hap = hap + n
    n = n + 1

print(hap)
