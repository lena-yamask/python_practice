input_num = input().split()
N = float(input_num[0])
M = input_num[1]
num_digits = "." + M + "f"
print(format(N, num_digits))
