# 큰 수 법칙 문제
############# My code ####################
n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse=True)  # 배열 역순으로 정렬
big = 0
cnt = 0

for i in range(m):
    if cnt == k:    # 똑같은 인덱스의 수를 k 번 사용했으면
        big += arr[1]  # 두 번째로 큰 수를 저장
        cnt = 0  # 두 번째로 큰 수를 한 번 사용했으니 다시 제일 큰 수를 사용하기 위해
    else:
        big += arr[0]  # 제일 큰 수를 저장
    cnt += 1  # cnt를 1씩 증가해서 k번 사용했는지 비교하기 위함

print(big)


########### 동빈나님 코드 #############
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]  # 가장 큰 수
second = data[n-2]  # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = m // (k+1) * k
count += m % (k+1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두 번째로 큰 수 더하기

print(result)