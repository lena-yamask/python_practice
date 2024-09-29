print('Hello','World') #'と"はあまり違わない
print("test", end=",") #改行の代わりに、endで指定した文字（空文字""や半角空白" "、","や"-->"も可能）で繋ぐ事もできる
print('hogehoge')
import random
print("サイコロ：",random.randint(1, 6)) #サイコロ

num = 1
num += 2  # num = num + 2 と同じ意味
print(num)

print(num ** 2) #べき乗は**

num = 1
num -= 1  # num = num - 1 と同じ意味
print(num)

num = 2
num *= 12  # num = num * 12 と同じ意味
print(num)

num = 2
num /= 2  # num = num / 2 と同じ意味
print(num)

num = 2
num //= 2  # num = num // 2 と同じ意味　//は小数点以下切り上げ
print(num)

num = 7
num %= 5  # num = num % 5 と同じ意味
print(num)

num = 5
num **= 2  # num = num ** 2 と同じ意味
print(num)

#上記numを使い回している例のように上書きもできるが、基本的には変数が書き変わってることに気付けないデメリットが大きいのでやらないこと。＋＝などはよく使う。

#Pythonでは、何もないことを「None」で表す
#print(num)
s = "Hello, World!"
print(s[0]) #indexは０から文字列の長さを超えない整数。
print(s[-1]) #負の数を指定すると、末尾を出力できる