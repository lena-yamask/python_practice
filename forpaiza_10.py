N, M = map(int, input().split())
A = input().split()
B = input().split()

for i in range(M):
    B_i = int(B[i])
    if i == 0:
        A_start = 0
        A_end = B_i - 1
    else:
        A_start += int(B[i-1])
        A_end = A_start + B_i - 1
    for A_i in range(A_start, A_end + 1):
        if A_i == A_end:
            print(A[A_i])
        else:
            print(A[A_i], end=" ")
