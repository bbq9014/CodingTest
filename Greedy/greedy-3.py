#숫자 카드 게임

################# My Code #################
n, m = map(int,input().split())

result = 0
tmp = list()

for i in range(n):
    data = list(map(int,input().split())) # 한 행을 입력
    tmp.append(min(data)) # 임시 리스트에 행의 최소값을 저장
result = max(tmp) # 임시 리스트에서 최대 값 저장

print(result)

################# 동빈나님 코드 min 사용 #################
n, m =map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data) # 한 행에서 최소값 저장
    result = max(result, min_value) # result의 값과 행에서 나온 최소값을 비교해서 더 큰 값을 저장

print(result)

############ 동빈나님 코드 2중 반복문용사용 ############
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a) # 한 행에 원소들 중 최소값 저장
    result = max(result, min_value) # result에 저장된 값과 행에서의 가장 최소값을 비교해서 큰 값을 저장

print(result)