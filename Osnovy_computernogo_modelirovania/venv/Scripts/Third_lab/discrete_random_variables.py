def form_polynom_first_order(a0, a1):
    def polynom(x):
        return a0 + a1*x
    return polynom


def form_polynom_third_order(a0, a1, a2, a3):
    def polynom(x):
        return a0 + a1*x + a2*pow(x, 2) + a3*pow(x, 3)
    return polynom


def form_logistics_curve(k, a, b):
    def formula(x):
        return 1/(k+a*pow(b,x))
    return formula



def fourth_algorithm(N, a0=1, q=5 ** 17, M=2 ** 42):
    values = [a0]
    for i in range(N):
        values.append((q * values[-1] % M))
    return list(map(lambda x: x/10000, values))


def third_algorithm(gamma0, N, k = None):
    if k == None:
        k = len(str(gamma0))
    values = [gamma0]
    for i in range(N):
        values.append(int(pow(values[-1], 2) / pow(10, k / 2)) % pow(10, k))
    return list(map(lambda x: x/(10**k), values))


def first_algorithm():
    pass


if __name__ == '__main__':
    print(third_algorithm(7153, 6))