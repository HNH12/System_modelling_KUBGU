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


if __name__ == '__main__':
    print(third_algorithm(7153, 6))