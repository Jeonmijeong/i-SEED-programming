# 6. 다음 각 코드를 실행한 후에, nn에 저장된 값을 쓰세요. 단, nn은 항상 보기의 5개 데이터가 저장되어 있다고 가정합니다.
nn_1 = [100, 200, 300, 400, 500]
nn_1[1] = 777
print("(1) :", nn_1)

nn_2 = [100, 200, 300, 400, 500]
nn_2[1] = [444, 555]
print("(2) :", nn_2)

nn_3 = [100, 200, 300, 400, 500]
nn_3[1:4] = [444, 555]
print("(3) :", nn_3)

nn_4 = [100, 200, 300, 400, 500]
nn_4[2:] = []
print("(4) :", nn_4)
