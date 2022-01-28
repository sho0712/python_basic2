"""
課題B-6: N面サイコロの反復試行
N面サイコロをM回振ったときの結果を表示してください
N, M は正の整数とします
N, M はユーザーからの入力を利用すること
実行例
サイコロの面の数は?: 8
何回振りますか?: 20
[6, 6, 8, 5, 1, 6, 4, 4, 3, 4, 7, 5, 7, 1, 4, 2, 5, 7, 1, 7]
"""

import random

dice_face = int(input("サイコロの面の数は?: "))
dice_roll = int(input("何回振りますか?: "))


def dice():
    if dice_face >= 1 and dice_roll >= 1:
        dice_trial = [random.randint(1, dice_face) for d in range(1, dice_roll + 1)]
        return dice_trial
    else:
        raise ValueError("正の整数(1以上)を入力してください")


print(dice())