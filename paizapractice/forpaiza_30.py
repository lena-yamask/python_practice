N = int(input())
M = [0] * N

for i in range(N):
    M[i] = int(input())

for i in range(N):
    print("{:>3}".format(M[i]))
