"""
課題B-2: 九九表の拡張
要件
下記のような出力が得られる kuku_2.py を実装してください
任意の行数および任意の列数での掛け算の結果が得られます
出力例1
$ python kuku_2.py
行数を入力してください: 4
列数を入力してください: 6
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
出力例2
$ python kuku_2.py
行数を入力してください: 12
列数を入力してください: 12
1 2 3 4 5 6 7 8 9 10 11 12
2 4 6 8 10 12 14 16 18 20 22 24
3 6 9 12 15 18 21 24 27 30 33 36
4 8 12 16 20 24 28 32 36 40 44 48
5 10 15 20 25 30 35 40 45 50 55 60
6 12 18 24 30 36 42 48 54 60 66 72
7 14 21 28 35 42 49 56 63 70 77 84
8 16 24 32 40 48 56 64 72 80 88 96
9 18 27 36 45 54 63 72 81 90 99 108
10 20 30 40 50 60 70 80 90 100 110 120
11 22 33 44 55 66 77 88 99 110 121 132
12 24 36 48 60 72 84 96 108 120 132 144
"""

number_i = int(input("行数を入力してください:"))
number_j = int(input("列数を入力してください:"))

for i in range(1, number_i + 1):
    for j in range(1, number_j + 1):
        print(i * j, end=' ')
    print()