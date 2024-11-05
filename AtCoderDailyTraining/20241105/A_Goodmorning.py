# input
A, B, C, D = map(int, input().split())

# 起床時間の比較計算 高橋＜青木 かを調べる
# 高橋ー＞A時B分
# 青木ー＞C時D分1秒
if A < C:
    print("Takahashi")
elif A > C:
    print("Aoki")
else:  # A==C
    if B <= D:
        print("Takahashi")
    else:
        print("Aoki")
