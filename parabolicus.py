from matplotlib import pyplot as plt
from numpy import sin, exp, pi


def solve_parabolic(start, border_left, border_right, source, ts, te):
    """
    start -- ��������� �������
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
    r = 0.45 # < 0.5
    tau = r * xi ** 2

    # �����, ��������� ��� �������
    v = list(u)

    # ������� �����
    t = ts

    while t < te:
        # �������� �������� � �������� �� ��������� �����
        for i in range(1, n):
            v[i] = (1 - 2 * r) * u[i] +\
                    r * (u[i-1] + u[i+1]) +\
                    tau * source(i * xi, t)
        # �������� �������� �� �����
        a0, b0, c0 = border_left(t)
        a1, b1, c1 = border_right(t)
        v[0] = (c0 - v[1] * a0 / xi) / (b0 - a0 / xi)
        v[n] = (c1 + v[n-1] * a1 / xi) / (b1 + a1 / xi)
        # ��� ������� ���������
        u, v = v, u
        # ���������� �������
        t += tau

    return u

# ���������� ������� �� ������� ������ � ������������� ���������� � �������
# ����� � ���������� ������� ������� ����������� �������� ������ ����� �������
# �����������. ��� ���� ����� ��� ����� ������� � �������� ������� �
# �����������, � ������ -- ���������������. ������ ������� ���������� ���������
# ���������� ��������� �������� �����. ��������� ���������� �������������
# ���������� � �������

n = 100

# ����� ��������� �������
u = [0.0 for i in range(n + 1)]

# ���������
locked = lambda t: [0.0, 1.0, 0.0]           # ������� � �����������
free =   lambda t: [1.0, 0.0, 0.0]           # ������������������ �����
source = lambda x, t: 1 if abs(x-0.5) < 1.0 / n else 0  # "��������" �������� ����������

X = [1.0 / n * i for i in range(n+1)]

# ������� �������
plt.plot(X, u)

dt = 0.1
for i in range(7):
    u = solve_parabolic(u, locked, free, source, i * dt, (i + 1) * dt)
    plt.plot(X, u)

# ������ ��� ���
plt.xlabel('distance')
plt.ylabel('temperature')
plt.title('The temperature distribution in the rod')
plt.show()
