# input
N = int(input())
A = input().split()  # list型

# Bの計算
for i in range(1, N):
    # B_i = A_i * A_i+1
    # Aのリストが０始まりなので、Aはインデックスを-1して計算と登録を行う
    B_i = int(A[i - 1]) * int(A[i])

    # 出力部
    if i == N - 1:
        print(B_i)
    else:
        print(B_i, end=" ")
