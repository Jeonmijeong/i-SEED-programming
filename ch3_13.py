# 13. 오류가 발생하는 것을 모두 고르고, 그 이유를 간단히 설명하세요.
int('1002', 2) # 2진수는 "0, 1"로만 표현 → "2" X
int('1008', 8) # 8진수는 "0 ~ 7"로만 표현 → "8" X
int('AAFG', 16) # 16진수는 "0 ~ 9, A ~ F"로만 표현 → "G" X
