# Q) 시각
# 완전 탐색 문제! brute forcing

n = int(input("시각 입력 : "))
cnt =0

for i in range(n+1):
    for j in range(60):
        for z in range(60):
            if '3' in str(i) + str(j) + str(z):
                cnt += 1
print(cnt)