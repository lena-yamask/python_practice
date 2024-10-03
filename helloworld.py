import random
print('Hello', 'World')  # 'と"はあまり違わない
print("test", end=",")  # 改行の代わりに、endで指定した文字で繋ぐ事もできる
# 空文字""や半角空白" "、や"-->" も可能
print('hogehoge')
print("サイコロ：", random.randint(1, 6))  # サイコロ

num = 1
num += 2  # num = num + 2 と同じ意味
print(num)

print(num ** 2)  # べき乗は**

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

# 上記numを使い回している例のように上書きもできるが、基本的には変数が書き変わってることに気付けないデメリットが大きいのでやらないこと。＋＝などはよく使う。

# Pythonでは、何もないことを「None」で表す
# print(num)
s = "Hello, World!"
print(s[0])  # indexは０から文字列の長さを超えない整数。
print(s[-1])  # 負の数を指定すると、末尾を出力できる
print(s[1:4])  # s[i:j]でiからj-1までの部分文字列の取得
print(s[:5])  # s[:j]で０からj-1までを取得
print(s[1:])  # s[i:]でiから末尾までを取得

print(len(s))  # lenで文字列の長さを取得

s1 = "Hello"
s2 = "World!"
print(s1 + s2, s1, s2)  # +で文字列を結合できる
s3 = "abc "
s3 += "def"
print(s3)

hanpuku = "abc"
print(hanpuku * 3)  # ＊の回数分、反復
hanpuku *= 2
print(hanpuku)

time = "10"
place = "会議室 A"
print(f"{time}時から{place}で会議がおこなわれる。")  # f文字列という使い方。"の直前にfをかく

# str = input()  # 入力文字列を１行取得してstrに入れる
# str2 = input().strip()  # 前後の空白を取り除いて取得
# str3 = input().split()  # 文字列を分割して取得

# input_line = int(input())
# for i in range(input_line):
#     s = input().rstrip().split(' ')
#     print("hello = "+s[0]+" , world = "+s[1])
time = 10
print(str(time) + "時")  # 数字->文字列

strtoint = "3"
print(int(strtoint) * 2)  # 文字列ー＞数字（整数）
print(float(strtoint) * 2.0)  # 文字列ー＞数字（浮動小数点数）

li = [5, "a", ["b", "c"]]  # リストの作り方
# 型はバラバラでも良いが推奨されず、型は統一した方がいい
# 空リストー＞s[]など要素を何も指定しないと作れる
print(li[1])  # インデックスを指定する
print(li[-1])
# li[i] iの値が負の時、リスト li の要素数 + i(=末尾からi番目)の要素を取得
# li[i:j] でiからj番目の要素を取得
# 文字列と同じように、インデックス指定省略可能
print(li[:])  # 先頭から末尾まで取得
print(len(li))  # リストの長さを取得
# a + b のようにリスト a とリスト b を結合すると、新しいリストが作成される
# li * n のようにリスト li を n 回反復すると、新しいリストが作成される

# li.append(e) のようにリストの append メソッドを使うと、
# リスト li の末尾に要素 e を追加することができる
print(li.append(4))
# li.pop() のようにリストの pop メソッドを使うと、
# リスト li の末尾の要素を削除して、その値を取得することができる
print(li.pop())

# li.remove(e) でリスト li から要素 e を削除することができる
# リスト li の要素として e が複数含まれる場合、最初に現われるものを削除する
li.remove("a")
print(li, len(li))
# del li[i] でリスト li のインデックス i の要素を削除することができる
del li[1]
print(li, len(li))
# del li[i:j] で i から j-1 までの要素を削除

li2 = [1, 3, 2]
print(sorted(li2))  # 昇順でソート（上書きしない）
li2.sort()  # 昇順（小さい順）に破壊的ソート（上書き）
print(li2)
li3 = ["apple", "cat", "banana"]
print(sorted(li3, reverse=True))  # 降順でソート（上書きしない）
li3.sort(reverse=True)  # 降順で破壊的ソート（上書き）
# 異なる型が混在するリストは、ソート/破壊的ソートはできない

li4 = ["A", "B", "C"]
print(" ".join(li))
print(",".join(li))
print("".join(li))
# s.join(li) 文字列 s を区切り文字として、リスト li の各要素を結合

# 文字列ー＞リスト
s = "hello"
print(list(s))

s = "apple,banana,cat"
print(s.split(","))  # ['', 'pple,b', 'n', 'n', ',c', 't']
# s.split(t) 文字列 s を文字列 t で区切ったときにできる
# 各文字列を要素とするリストを生成できる

# タプル
# イミュータブルなので、変更不可
# 追加・変更などしたい場合はタプルを新しく作る
lunchset = ("chees burger", 750)
# パッキング　複数の値をタプルにまとめること
# ()は省略可能。要素がない or 複数のタプルを同時に書く場合は省略不可。
print(lunchset)
print(lunchset[1])
# tuple[i:j] タプルのiからj-1番目の要素を取得
food, price = lunchset
# アンパッキング　タプルの各要素を分解して代入
# 取り出し先の名前をわかりやすくつけることができる
tuple(range(10))  # 0から９までの整数を格納したタプルを作成

alphabet = tuple("ABCDEFG")
first, second, *rest, last = alphabet
print(first)  # A
print(rest)  # C, D, E, F
print(last)  # G
# 先頭や末尾の要素だけ取り出したい時に使う＊

# リストとタプル、タプル同士などを組み合わせる事も可能
menu = [("burger", 110, 234.5), ("potato", 150, 226.7)]
# この例は、リストの中にタプル２つを入れ子にしている。カッコは省略不可。
menu.append(("shake", 120, 218.9))
# menu自体はリストなので、追加・変更・削除ができる
print(menu[1])
name, price, calorie = menu[1]
print(calorie)

# タプルの結合
turple_a = (2, 4, 6)
turple_b = ("apple", "banana", "cat")
print(turple_a + turple_b)
turple_a += turple_b
print(turple_a)

# タプルの反復
t1 = (1, "apple")
print(t1 * 2)  # 新しいタプルとして作成されている

# if文の作成
# if 条件式:
#   処理A
# else:
#   処理B

# elif文
# if 条件式:
#   処理A
# elif 条件式:
#   処理B
# else:
#   処理C
a = 11
if a < 10:
    print("1桁")
elif a < 100:
    print("2桁")
else:
    print("3桁以上")

# pass文 その節を書く必要はあっても、何も処理をしたくない場合に使う
if a < 0:
    pass  # 何も処理をしない
elif a < 10:
    print("1桁")
elif a < 100:
    print("2桁")
else:
    print("3桁以上")
