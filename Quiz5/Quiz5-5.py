import pyxel

pyxel.init(200, 200)  # 画面の表示

a = 0
b = 0
# 変数の設定


def update():
    global a
    global b
    b += 1  # 徐々にスピードを上げていく変数としてbを設定
    a += 10 + b  # aが増えることで位置が移動する
    a = a % 200  # 範囲外に円が出ないように設定している。


def draw():
    global a
    global b
    pyxel.cls(7)  # 背景色の指定。白色
    pyxel.circ(a, a, 10, 0)  # 円の座標、および大きさと色をしている。


pyxel.run(update, draw)  # 上の関数を動かす。
