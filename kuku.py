N = int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        num_mul_table = i * j
        if j == N:
            print(num_mul_table)
        else:
            print(num_mul_table, end=" ")
