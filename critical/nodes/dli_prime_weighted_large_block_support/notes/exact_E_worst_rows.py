import numpy as np, math
def exact_E(q, NP=64):
    N = NP // 2
    # pinned omega
    def spr(q):
        # q-1 factor by trial division (q ~ 1e5-2e5, fine)
        n = q - 1; fs = set()
        d = 2
        while d * d <= n:
            while n % d == 0:
                fs.add(d); n //= d
            d += 1
        if n > 1: fs.add(n)
        g = 2
        while any(pow(g, (q-1)//p, q) == 1 for p in fs):
            g += 1
        return g
    g = spr(q)
    omega = pow(g, (q - 1) // NP, q)
    xs = np.array([pow(omega, y, q) for y in range(N)], dtype=np.int64)
    lam = np.arange(q, dtype=np.int64)
    # a_y(lambda) = lambda * x_y mod q ; process in chunks
    E = 0.0
    for lo in range(0, q, 20000):
        chunk = lam[lo:lo+20000, None] * xs[None, :] % q
        c = np.cos(np.pi * chunk / q) ** 2
        E += np.exp(np.log(np.maximum(c, 1e-300)).sum(axis=1)).sum()
    r = q / 2.0**N
    W_from_E = E / r - 1
    return E, math.log2(E), r
for q, k in [(110849, 4), (100609, 5), (204353, 7), (65537, '-')]:
    E, log2E, r = exact_E(q)
    print(f"q={q} (k_indep={k}): E = {E:.8f}, log2 E = {log2E:.3e} bits, r = {r:.3e}")
