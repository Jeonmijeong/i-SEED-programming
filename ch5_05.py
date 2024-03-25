# 5. 다음 코드의 2~5행을 삼항 연산자로 변경한 것으로 옳은 것을 고르세요.

# num = 5
# if num % 2 == 0 :
#     res = '짝수'
# else :
#     res = '홀수'
# print(res)

res = '짝수' if num % 2 == 0 else '홀수'
print(res)
