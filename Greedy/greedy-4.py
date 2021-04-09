# 1이 될 때까지
""" My Code """
n, k = map(int, input().split())

result = 0

while n != 1:
    if n % k == 0:  # N이 K로 나눠 떨어지면 나누기
        n //= k
    else:  # 아니면 - 1
        n -= 1
    result += 1  # 횟수 1 증가

print(result)

""" 동빈나님 Code """
n, k = map(int, input().split())
result = 0
while True:
    target = (n//k)*k  # N이 K로 나누어 떨어질 수 있는 최대값
    result += (n - target)  # n - target 만큼 1을 빼줘야하므로 result에 추가
    n = target
    # N이 K 보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)
