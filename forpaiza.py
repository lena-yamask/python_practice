N = int(input())
M_list = [int(x) for x in input().split()]

for i in range(1, N + 1):
    M_i = M_list[i - 1]
    for j in range(1, M_i + 1):
        if j == M_i:
            print(j)
        else:
            print(j, end=" ")
