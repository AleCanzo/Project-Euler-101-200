import numpy as np
import matplotlib.pyplot as plt

index = 0
TRIANGLES = []
ax = None

def contains_origin(u, v, w):

    v = v - u
    w = w - u
    o = -u

    d = v[0]*w[1] - v[1]*w[0]

    weight_u = (o[0]*(v[1] - w[1]) + o[1]*(w[0] - v[0]) + v[0]*w[1] - v[1]*w[0]) / d
    weight_v = (o[0]*w[1] - o[1]*w[0]) / d
    weight_w = (o[1]*v[0] - o[0]*v[1]) / d

    if (0 <= weight_u <= 1 and
        0 <= weight_v <= 1 and
        0 <= weight_w <= 1):
        return True

    return False


def viz_triangle(triangles):
    global TRIANGLES, ax
    TRIANGLES = triangles

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect("key_press_event", on_key)

    draw_triangle(index)

    plt.show()


def draw_triangle(i):
    ax.clear()

    u, v, w = TRIANGLES[i]

    x = [u[0], v[0], w[0], u[0]]
    y = [u[1], v[1], w[1], u[1]]

    ax.plot(x, y)
    ax.scatter(0,0)

    ax.axhline(0)
    ax.axvline(0)

    ax.set_aspect('equal')
    ax.set_title(f"Triangolo {i+1}/{len(TRIANGLES)}")

    plt.draw()


def on_key(event):
    global index

    if event.key == "right":
        index = (index + 1) % len(TRIANGLES)

    elif event.key == "left":
        index = (index - 1) % len(TRIANGLES)

    draw_triangle(index)


if __name__ == "__main__":

    coordinates = np.loadtxt("101-200/0102_triangles.txt", dtype=int, delimiter=",")

    triangles = []
    c = 0

    for i in range(1000):
        u = coordinates[i][0:2]
        v = coordinates[i][2:4]
        w = coordinates[i][4:6]

        if contains_origin(u, v, w):
            c += 1
        else:
            triangles.append([u, v, w])

    viz_triangle(triangles)

    print("Triangoli che contengono l'origine:", c)
