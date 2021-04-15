# 왕실의 나이트
""" My Code """
position = input()  # a1

count = 0

x = position[0]  # a
y = position[1]  # 1

# 원래 나이트 움직임 경우의 수는 8가지
# 위2왼1, 위2오1, 오2위1, 오2아1, 아2왼1, 아2오1, 왼2위1, 왼2아1
dx = [-1, 1, 2, 2, -1, 1, -2, -2]  # 수평으로 이동
dy = [-2, -2, -1, 1, 2, 2, -1, 1]  # 수직으로 이동

# 나이트의 모든 움직임 완전탐색
for i in range(8):
    # 경우의 수마다 나이트의 위치 예상
    nx = ord(x)+dx[i]
    ny = ord(y)+dy[i]
    # 움직인 뒤에 체스판 범위 안에 나이트가 존재한다면 카운트 증가
    if ord('a') <= nx <= ord('h') and ord('1') <= ny <= ord('8'):
        count += 1

print(count)

""" 동빈나님 코드 """
# 현재 나이트의 위치 입력
input_data = input()
row = int(input_data[1])
column = int(input_data[0]) - int(ord('a'))+1

steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
