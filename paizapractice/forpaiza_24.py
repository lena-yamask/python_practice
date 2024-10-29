Q = int(input())

for i in range(Q):
    input_num = input().split()
    N = float(input_num[0])
    M = input_num[1]

    print("{:.{}f}".format(N, M))
