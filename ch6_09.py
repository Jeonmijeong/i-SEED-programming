# 9. for 문을 사용해서 3333부터 9999까지의 숫자 중에서 1234의 배수의 합계를 구하되, 100000(십만)이 넘기 직전까지만 합계를 구하는 코드를 작성하세요. 단, 코드에는 continue와 break를 모두 사용해서 작성하세요.

hap = 0
for n in range(3333,9999) :
    if n % 1234 != 0 :
        continue

    hap = hap + n

    if hap >= 100000 :
        hap = hap - n
        break

print(hap)
