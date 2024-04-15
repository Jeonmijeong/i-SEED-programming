1. 다음 보기를 입력과 관련된 함수와 출력과 관련된 함수로 분류하세요.

input(), print(), write(), read(), readline(), writeline(), readlines()

정답 : 입력 - input(), read(), readline(), readlines() / 출력 - print(), write(), writeline()

2. 다음은 파일의 처리단계입니다. 순서대로 나열한 것이 맞는 것을 고르세요.

A. 파일 열기
B. 파일 쓰기
C. 파일 읽기
D. 파일 닫기

정답 : ① A→C→B→D

3. 파일의 열기 모드에 대한 설명입니다. 거리가 먼 것을 모두 고르세요.

 ① 생략하면 쓰기 모드가 기본으로 설정된다. 
 ② r+는 읽기/쓰기 겸용 모드이다.
 ③ a는 쓰기 모드이다. 기존 파일이 있으면 삭제하고 새로 만든다.
 ④ t는 텍스트 모드이다.
 ⑤ b는 이진 파일 모드이다.
 ⑥ tb는 텍스트 파일 겸 이진 파일 모드 공용이다.

정답 : ① - 생략하면 읽기 모드가 기본으로 설정된다. / ③ - a는 쓰기 모드이다. 기존 파일이 있으면 끝에 내용을 추가한다. / ⑥ - tb는 없다.

4. 다음은 data1.txt 파일에서 1개 행만 읽어서 출력하는 코드입니다. 빈칸을 채우세요.

inFp = open("C:/Temp/data1.txt", "r")

inStr = inFp.readline()
print(inStr, end="")

inFp.close()

6. 다음은 파일을 복사하는 코드입니다. 빈칸을 채우세요.

inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.readlines(inStr)

inFp.close()
outFp.close()
