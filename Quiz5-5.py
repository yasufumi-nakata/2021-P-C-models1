import pyxel

pyxel.init(200, 200)

a = 0
b = 0


def update():
    global a
    global b
    b += 1
    a += 10 + b
    a = a % 200


def draw():
    global a
    global b
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)


pyxel.run(update, draw)
