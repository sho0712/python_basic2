"""
課題B-5:基本統計量の計算
スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
合計値
最大値
最小値
平均値
ただし、組み込み関数やライブラリは使わないこと(sum()やnp.mean()など)
1つの統計量につき、それ専用の関数を実装すること
実行例
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""

# split()関数は文字列を指定した内容でリスト分割
# inputの入力値はstr型 ⇒ map関数で型変換(int型へ)
# その後list()関数でmapオブジェクトをリスト化
input_n = list(map(int, input("データを入力してください(スペース区切り) > ").split()))


def sum():
    sum_n = 0
    for n in input_n:
        sum_n += n
    return sum_n


def max():
    max_n = input_n[0]
    for n in input_n:
        if n > max_n:
            max_n = n
    return max_n


def min():
    min_n = input_n[0]
    for n in input_n:
        if n < min_n:
            min_n = n
    return min_n


def ave():
    ave = sum() // len(input_n)
    return ave


print(f"合計値: {sum()}")
print(f"最大値: {max()}")
print(f"最小値: {min()}")
print(f"平均値: {ave()}")
