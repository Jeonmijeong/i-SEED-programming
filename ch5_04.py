# 4. 다음은 장학생, 합격, 불합격으로 구분하는 중첩 if 문입니다. 이를 if ~ elif 문으로 변경하세요.

# score = int(input("점수를 입력하세요 : "))

# if score >= 90 :
#     print("장학생", end='')
# else :
#     if score >= 60 :
#         print("합격", end='')
#     else :
#         print("불합격", end='')

# print("입니다. ^^")

score = int(input("점수를 입력하세요 : "))

if score >= 90 :
    print("장학생", end='')
elif score >= 60 :
    print("합격", end='')
else :
    print("불합격", end='')

print("입니다. ^^")
