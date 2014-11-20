from matplotlib import pyplot as plt
from numpy import sin, exp, pi


def solve_hyperbolic(start, der, border_left, border_right, source, ts, te):
    """
    start -- ��������� �������
    der -- ��������� ������� �� �����������
    border_*(t) -- ���������
    source(x, t) -- ������� ���������
    ts -- ����� ������ ������������
    te -- ����� ����� ������������
    """
    u = list(start)

    # ���������� ����� �� ��� x
    n = len(u) - 1
    xi = 1.0 / n

    # ��� �� ������� (�� ������� �������)
    r = 0.95 # < 1
    tau = xi * r ** 0.5

    # �����, ��������� ��� �������
    v = list(u)
    w = list(u)

    # ��������� ��� �� ���������� ������� �� �����������
    v = [ui + tau * der[i] for i, ui in enumerate(u)]

    # ������� �����
    t = ts

    while t < te:
        # �������� �������� � �������� �� ��������� �����
        for i in range(1, n):
            w[i] = 2 * (1 - r) * v[i] +\
                    r * (v[i-1] + v[i+1]) -\
                    u[i] + tau * tau * source(i * xi, t)
        # �������� �������� �� �����
        a0, b0, c0 = border_left(t)
        a1, b1, c1 = border_right(t)
        v[0] = (c0 - v[1] * a0 / xi) / (b0 - a0 / xi)
        v[n] = (c1 + v[n-1] * a1 / xi) / (b1 + a1 / xi)
        # ��� ������� ���������
        u, v, w = v, w, u
        # ���������� �������
        t += tau

    d = [(v[i] - u[i]) / tau for i in range(n + 1)]
    return u, d

#

n = 100

# ����� ��������� �������
u = [sin(pi * i / n) for i in range(n + 1)]
der = [0] * (n+1)

# ���������
locked = lambda t: [0.0, 1.0, 0.0]  # ����������� �����
source = lambda x, t: 0

X = [1.0 / n * i for i in range(n+1)]

# ������� �������
plt.plot(X, u)

dt = 0.1
for i in range(10):
    u, der = solve_hyperbolic(u, der, locked, locked, source, i*dt, (i+1)*dt)
    plt.plot(X, u)

# ������ ��� ���
plt.xlabel('distance')
plt.ylabel('offset')
plt.title('vibrations of a string')
plt.show()
