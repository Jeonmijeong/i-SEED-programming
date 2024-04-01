# 8. 다음은 3개의 매개변수 중 기본값을 2개 설정하는 코드입니다. 빈칸을 채우세요.
def myFunc(p1=0, p2=0, p3=0):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 ==> ", myFunc())
print("매개변수가 1개로 호출 ==> ", myFunc(1))
print("매개변수가 2개로 호출 ==> ", myFunc(1, 2))
print("매개변수가 3개로 호출 ==> ", myFunc(1, 2, 3))
