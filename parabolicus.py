from matplotlib import pyplot as plt
from numpy import sin, exp, pi


def solve_parabolic(start, border_left, border_right, source, ts, te):
    """
    start -- начальное условие
    border_*(t) -- граничные
    source(x, t) -- функция источника
    ts -- время начала эксперимента
    te -- время конца эксперимента
    """
    u = list(start)

    # количество шагов на оси x
    n = len(u) - 1
    xi = 1.0 / n

    # шаг по времени (из условия Куранта)
    r = 0.45 # < 0.5
    tau = r * xi ** 2

    # копия, пригдится при расчёте
    v = list(u)

    # текущее время
    t = ts

    while t < te:
        # пересчёт значений в середине по разносной схеме
        for i in range(1, n):
            v[i] = (1 - 2 * r) * u[i] +\
                    r * (u[i-1] + u[i+1]) +\
                    tau * source(i * xi, t)
        # пересчёт значений на краях
        a0, b0, c0 = border_left(t)
        a1, b1, c1 = border_right(t)
        v[0] = (c0 - v[1] * a0 / xi) / (b0 - a0 / xi)
        v[n] = (c1 + v[n-1] * a1 / xi) / (b1 + a1 / xi)
        # нет времени объяснять
        u, v = v, u
        # обновление времени
        t += tau

    return u

# Рассмотрим решение на примере задачи о распределении температур в стержне
# Пусть у достаточно тонкого стержня отсутствуют тепловые потери через боковую
# поверхность. При этом левый его конец приведён в тепловой контакт с
# термостатом, а правый -- теплоизолирован. Внутри стержня посередине находится
# достаточно маленький источник тепла. Требуется определить распределение
# температур в стержне

n = 100

# задаём начальное условие
u = [0.0 for i in range(n + 1)]

# граничные
locked = lambda t: [0.0, 1.0, 0.0]           # контакт с термостатом
free =   lambda t: [1.0, 0.0, 0.0]           # теплоизолированный конец
source = lambda x, t: 1 if abs(x-0.5) < 1.0 / n else 0  # "точечный" источник посередине

X = [1.0 / n * i for i in range(n+1)]

# профиль функции
plt.plot(X, u)

dt = 0.1
for i in range(7):
    u = solve_parabolic(u, locked, free, source, i * dt, (i + 1) * dt)
    plt.plot(X, u)

# покажи мне это
plt.xlabel('distance')
plt.ylabel('temperature')
plt.title('The temperature distribution in the rod')
plt.show()
