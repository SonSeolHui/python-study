#리스트 안에는 데이터를 모을 수 있다.
T = [a, b, c, d, e,[A, B, C]]

#양수 인덱스는 왼쪽부터 0부터 세고, 음수의 경우 맨 오른쪽부터 -1로 시작한다.
#인덱싱은 리스트 안의 데이터를 찾아 불러오는 것을 말한다.

print('인덱스 0 :', t[0])
print('인덱스 -1 :', t[-1])

#리스트 안 데이터 변경하기
A = [1, 2, 3, 4, 5]
A[2]=5
print(A)

A[1]=A[1]+5
print(A)