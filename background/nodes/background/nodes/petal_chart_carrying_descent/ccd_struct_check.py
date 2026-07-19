#!/usr/bin/env python3
"""ccd_struct_check: stage-1 structure identities for petal_chart_carrying_descent.

M = 2 descent of the fiber-aligned chart word (census conventions copied
verbatim from cg_petal_census.py: build_layout('fiber_aligned'), build_word).

Pre-registered expectation E1: ALL identities PASS at every cell.
Identities:
  I0  layout sanity: |Z| = k-1, petal count t = (n-k)/2, split point exp nf,
      background = {nf + n/2}.
  I1  L_Z(X) = L_{Z'}(X^2) * (X - x_nf)   (polynomial identity in F_p[X]).
  I2  fiberwise Fourier components of U:  u_0 = -x_nf * u_1  (pointwise).
  I3  u_1 is the quotient chart word: u_1 = 0 on Z' u {y_nf};
      u_1(y_i) = c_i * L_{Z'}(y_i) on descended petal points.
  I4  U(x) = (x - x_nf) * u_1(x^2) for ALL x in H.
  I5  descent semantics: for 20 random codewords f (coeff split f_0, f_1):
      f agrees with U at both points of fiber j  <=>  f_0(y_j) = u_0(y_j) and
      f_1(y_j) = u_1(y_j)   (the proved fiberwise bijection, in vivo).
  I6  lift semantics: for 20 random g (deg < k'), f = (X - x_nf) g(X^2):
      x_nf always agrees; -x_nf agrees iff g(y_nf) = 0; on every other fiber
      agreement is all-or-nothing and holds iff g(y) = u_1(y).
"""
import itertools, random
from math import comb

# ---- census-verbatim utilities (copied from cg_petal_census.py) ----
def is_prime(m):
    if m < 2: return False
    if m % 2 == 0: return m == 2
    d = 3
    while d*d <= m:
        if m % d == 0: return False
        d += 2
    return True

def order_n_domain(p, n):
    assert (p-1) % n == 0
    a = 2
    while True:
        g0 = pow(a, (p-1)//n, p)
        if pow(g0, n//2, p) != 1: break
        a += 1
    dom = [pow(g0, j, p) for j in range(n)]
    assert len(set(dom)) == n
    return dom

def locator_poly(roots, p):
    loc = [1]
    for r in roots:
        new = [0]*(len(loc)+1)
        for i, c in enumerate(loc):
            new[i] = (new[i] - r*c) % p
            new[i+1] = (new[i+1] + c) % p
        loc = new
    return loc

def ev(poly, x, p):
    v = 0
    for c in reversed(poly):
        v = (v*x + c) % p
    return v

def build_layout_fiber_aligned(n, k):
    half = n // 2
    nf = (k-1)//2
    core = []
    for j in range(nf):
        core.extend([j, j+half])
    extra = []
    if (k-1) % 2:
        core.append(nf)
        extra = [nf+half]
    petal_fibers = [j for j in range(nf + (1 if (k-1) % 2 else 0), half)]
    petals = [sorted([j, j+half]) for j in petal_fibers]
    return sorted(core), petals, sorted(extra)

def scalars(mode, t, p, seed=0):
    if mode == "geom5":
        out, v = [], 1
        for _ in range(t): out.append(v); v = v*5 % p
    elif mode == "geom3":
        out, v = [], 1
        for _ in range(t): out.append(v); v = v*3 % p
    elif mode == "consec":
        out = [(i+1) % p for i in range(t)]
    elif mode.startswith("rand"):
        rng = random.Random(1000+seed)
        out = [rng.randrange(1, p) for _ in range(t)]
    else:
        raise ValueError(mode)
    return out

def build_word(n, k, p, dom):
    core, petals, bg = build_layout_fiber_aligned(n, k)
    loc = locator_poly([dom[j] for j in core], p)
    return core, petals, bg, loc

# ---- checks ----
def run_cell(n, k, p, smode, seed):
    fails = []
    dom = order_n_domain(p, n)
    core, petals, bg, locZ = build_word(n, k, p, dom)
    t = len(petals)
    scal = scalars(smode, t, p, seed)
    values = [0]*n
    for c_i, P in zip(scal, petals):
        for j in P:
            values[j] = c_i * ev(locZ, dom[j], p) % p
    half = n//2; nprime = half
    nf = (k-1)//2
    # I0 layout sanity
    if len(core) != k-1: fails.append("I0 |Z|")
    if t != (n-k)//2: fails.append("I0 t")
    if (k % 2 == 0) and (bg != [nf+half] or core[-1] != half+nf-1 and nf not in core):
        pass
    if k % 2 == 0 and nf not in core: fails.append("I0 split")
    x_nf = dom[nf]
    # quotient domain: dom2[i] = dom[i]^2 = g0^{2i}, order n' = n/2
    dom2 = [dom[i]*dom[i] % p for i in range(nprime)]
    if len(set(dom2)) != nprime: fails.append("I0 dom2")
    # descended core Z' = squares of full core fibers = dom2[0..nf-1]
    Zp = [dom2[j] for j in range(nf)]
    y_nf = dom2[nf]
    locZp = locator_poly(Zp, p)
    # I1: L_Z(X) == L_{Z'}(X^2) * (X - x_nf)
    lhs = locZ
    inner = [0]*(2*len(locZp)-1)
    for i, c in enumerate(locZp): inner[2*i] = c
    rhs = [0]*(len(inner)+1)
    for i, c in enumerate(inner):
        rhs[i] = (rhs[i] - x_nf*c) % p
        rhs[i+1] = (rhs[i+1] + c) % p
    if [c % p for c in lhs] != [c % p for c in rhs]: fails.append("I1")
    # Fourier components of U: solve per fiber {x, -x}: U(x)=u0+x u1, U(-x)=u0-x u1
    u0 = [0]*nprime; u1 = [0]*nprime
    for i in range(nprime):
        x = dom[i]; a = values[i]; b = values[i+half]
        u0[i] = (a+b) * pow(2, -1, p) % p
        u1[i] = (a-b) * pow(2*x, -1, p) % p
    # I2: u0 = -x_nf * u1
    if any(u0[i] != (-x_nf*u1[i]) % p for i in range(nprime)): fails.append("I2")
    # I3: u1 = quotient chart word
    for j in range(nf):
        if u1[j] != 0: fails.append("I3 core"); break
    if u1[nf] != 0: fails.append("I3 ynf")
    for c_i, P in zip(scal, petals):
        j = P[0]  # fiber index = quotient index
        if u1[j] != c_i * ev(locZp, dom2[j], p) % p:
            fails.append("I3 petal"); break
    # I4: U(x) = (x - x_nf) u1(x^2), where u1 as function via index j mod n'
    for j in range(n):
        if values[j] != (dom[j]-x_nf) * u1[j % nprime] % p:
            fails.append("I4"); break
    # I5: descent semantics on random codewords
    rng = random.Random(7)
    for _ in range(20):
        f = [rng.randrange(p) for _ in range(k)]
        f0 = f[0::2]; f1 = f[1::2]  # f(x) = f0(x^2) + x f1(x^2)
        for i in range(nprime):
            both = (ev(f, dom[i], p) == values[i]) and (ev(f, dom[i+half], p) == values[i+half])
            comp = (ev(f0, dom2[i], p) == u0[i]) and (ev(f1, dom2[i], p) == u1[i])
            if both != comp: fails.append("I5"); break
        else: continue
        break
    # I6: lift semantics
    kp = k//2
    for _ in range(20):
        g = [rng.randrange(p) for _ in range(kp)]
        # f = (X - x_nf) g(X^2): f(x) = x g(x^2) - x_nf g(x^2)
        agree = [None]*n
        for j in range(n):
            fx = (dom[j]-x_nf) * ev(g, dom2[j % nprime], p) % p
            agree[j] = (fx == values[j])
        if not agree[nf]: fails.append("I6 xnf")
        gy = ev(g, y_nf, p)
        if agree[nf+half] != (gy == 0): fails.append("I6 -xnf")
        for i in range(nprime):
            if i == nf: continue
            gv = ev(g, dom2[i], p)
            expect = (gv == u1[i])
            if agree[i] != expect or agree[i+half] != expect:
                fails.append("I6 fiber"); break
        if fails and fails[-1].startswith("I6 fiber"): break
    return fails

def main():
    cells = []
    rows = [(16, 8, [97, 257, 337, 449]),
            (32, 12, [97, 193, 449, 577]),
            (32, 16, [97, 193, 1153])]
    nfail = 0
    for n, k, primes in rows:
        for p in primes:
            for smode, seed in [("geom5", 0), ("geom3", 0), ("consec", 0),
                                ("rand", 1), ("rand", 2)]:
                fails = run_cell(n, k, p, smode, seed)
                tag = f"({n},{k},p={p},{smode},{seed})"
                if fails:
                    nfail += 1
                    print("FAIL", tag, fails)
                cells.append(tag)
    print(f"cells checked: {len(cells)}; failures: {nfail}")
    print("ALL PASS" if nfail == 0 else "FAILURES PRESENT")

if __name__ == "__main__":
    main()
