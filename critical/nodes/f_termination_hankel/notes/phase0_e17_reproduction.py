# Phase-0 GATE: reproduce the E17 signature on the FAITHFUL object.
# Flat P = ker(Hankel(S, t=3, j=5)), S in F_17^8 (the v12 extractor syndrome
# window); evaluate P on mu_16; weight-2 dual word = proportional column pair
# {x_a, x_b}; classify by cyclic exponent-diameter. E17 = a NON-COSET,
# adjacent (diameter-1) weight-2 support. If those appear, object validated.
import itertools, random
random.seed(0)
P = 17; N = 16; K = 8; J = 5; T = 3   # t+j = 8 = n-k, j+1=6, A=k+t=11
g = 3                                  # ord(3) = 16 mod 17
pts = [pow(g, a, P) for a in range(N)]  # x_a = 3^a
Mpull = [2, 4, 8]                       # x -> x^M pullbacks, M | gcd(16,8)=8

def kernel_basis(rows, ncol):
    M = [r[:] for r in rows]; piv = {}; r = 0
    for c in range(ncol):
        pr = next((i for i in range(r, len(M)) if M[i][c] % P), None)
        if pr is None: continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], P-2, P); M[r] = [(x*inv) % P for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % P:
                f = M[i][c]; M[i] = [(a-f*b) % P for a, b in zip(M[i], M[r])]
        piv[c] = r; r += 1
    basis = []
    for fc in [c for c in range(ncol) if c not in piv]:
        v = [0]*ncol; v[fc] = 1
        for c, rr in piv.items(): v[c] = (-M[rr][fc]) % P
        basis.append(v)
    return basis

def col_at(basis, x):                   # evaluation column at point x: (f(x))_{f in basis}
    return tuple(sum(b[d]*pow(x, d, P) for d in range(len(b))) % P for b in basis)

def proportional(u, v):
    # nonzero columns u,v proportional over F_p?
    if all(t == 0 for t in u) or all(t == 0 for t in v): return False
    r = None
    for a, b in zip(u, v):
        if a or b:
            if a == 0 or b == 0: return (a == 0 and b == 0)
            rr = (a * pow(b, P-2, P)) % P
            if r is None: r = rr
            elif rr != r: return False
    return True

def cyc_diam(a, b):
    d = abs(a-b); return min(d, N-d)

def is_pullback_pair(a, b):
    return any((a % (N//M)) == (b % (N//M)) and a != b for M in Mpull)  # same x^M fiber

diam_hist = {}; noncoset_adjacent = 0; total_w2 = 0; examples = []
TRIALS = 60000
for _ in range(TRIALS):
    S = [random.randrange(P) for _ in range(T+J)]
    rows = [[S[i+c] for c in range(J+1)] for i in range(T)]
    basis = kernel_basis(rows, J+1)
    if not basis: continue
    cols = [col_at(basis, x) for x in pts]
    for a, b in itertools.combinations(range(N), 2):
        if proportional(cols[a], cols[b]):
            total_w2 += 1
            d = cyc_diam(a, b); diam_hist[d] = diam_hist.get(d, 0) + 1
            if not is_pullback_pair(a, b):
                if d == 1:
                    noncoset_adjacent += 1
                    if len(examples) < 5: examples.append((a, b))

print(f"trials={TRIALS}  weight-2 supports found={total_w2}")
print("cyclic-diameter histogram:", dict(sorted(diam_hist.items())))
print(f"NON-coset adjacent (diam-1) weight-2 supports: {noncoset_adjacent}")
print("examples (exponent pairs):", examples)
print("E17 SIGNATURE REPRODUCED" if noncoset_adjacent > 0 else "signature NOT found")
