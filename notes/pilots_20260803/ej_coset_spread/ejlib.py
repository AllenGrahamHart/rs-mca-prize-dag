"""ejlib -- independent engine for the E_j coset-spread pilot.

Everything here is re-derived from the window system (PREREG section 1) and
cross-checked against gamma_j2_close/g2lib.py, which is imported READ-ONLY as a
third opinion (its `classify_lean` is the banked classifier; its `Scan` is the
theory-free ground truth).

Conventions (PREREG section 0):
    r  := n-k-w        size of an MC family member T_MC
    r' := n-A = r-1    size of an admissible T          (A = k+w+1)
    gamma := (-1)^{r'} c

My reformulation of admissibility for  j < w  (claimed equivalent to the
alpha_i + z beta_i = 0 window system; the equivalence is MACHINE-VERIFIED in
x1_identities.py, falsifier F-A):

    lam := e_j(T) != 0,   z := (-1)^{j+1} lam
    (Q3)  e_t(T) = lam . e_{t-j}(T)                    t = j+1 .. w-1
    (Q5)  e_j(T) . e_j(T^{-1}) = 1
    (Q6)  e_rho(T^{-1}) = e_{j-1}(T^{-1}) . e_{j-1-rho}(T)   rho = 0 .. j-2
    (Q8)  gamma = - prod(T) . e_{j-1}(T^{-1}) . e_j(T)

The BAND family (level L0) is (Q3) alone with lam != 0 -- the sub-system that
rigidity (CLAIM H) actually uses.  It is populous where the full system is not,
which is how route (2) gets tested at w >= 2j+1 (PREREG D-7).
"""

import os
import sys
from itertools import combinations

sys.dont_write_bytecode = True

_GAMMA_DIR = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), "gamma_j2_close")
sys.path.insert(0, _GAMMA_DIR)
import g2lib as G                                                # noqa: E402


# --------------------------------------------------------------- re-exports
is_prime = G.is_prime
primitive_root = G.primitive_root
make_domain = G.make_domain
mu_n_set = G.mu_n_set
coset_rep = G.coset_rep
inv_table = G.inv_table
esym = G.esym
comb = G.comb
Ledger = G.Ledger
Scan = G.Scan
pencil_words = G.pencil_words
mc_cosets = G.mc_cosets
mc_family = G.mc_family
mc_c_from_gamma = G.mc_c_from_gamma
neg_Hj = G.neg_Hj
INF = G.INF


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# ------------------------------------------------------- subset enumeration
def enumerate_subsets(H, q, n, rp, TOP, BOT):
    """Yield (Tidx_tuple, eT[0..TOP-1], eTi[0..BOT-1], prod) for every
    rp-subset of H.  eT = elementary symmetric of T, eTi = of T^{-1}.
    Prefix-shared, so the cost is one modular fma per (node, coefficient)."""
    IT = inv_table(q)
    invH = [IT[x] for x in H]
    out = []

    def rec(pos, eT, eTi, pr, chosen):
        if len(chosen) == rp:
            out.append((tuple(chosen), eT, eTi, pr))
            return
        need = rp - len(chosen)
        for p in range(pos, n - need + 1):
            x, xi = H[p], invH[p]
            e2 = eT[:]
            for t in range(TOP - 1, 0, -1):
                if e2[t - 1]:
                    e2[t] = (e2[t] + x * e2[t - 1]) % q
            i2 = eTi[:]
            for t in range(BOT - 1, 0, -1):
                if i2[t - 1]:
                    i2[t] = (i2[t] + xi * i2[t - 1]) % q
            chosen.append(p)
            rec(p + 1, e2, i2, (pr * x) % q, chosen)
            chosen.pop()

    rec(0, [1] + [0] * (TOP - 1), [1] + [0] * (BOT - 1), 1, [])
    return out


# ----------------------------------------------------- my own classifiers
def band_solutions(H, q, n, rp, w, j):
    """L0: every rp-subset T of H with lam := e_j(T) != 0 and
    e_t(T) = lam e_{t-j}(T) for t = j+1..w-1.  Requires j < w.
    Returns [{'Tidx','lam','z','eT'}]."""
    assert j < w, "band family is empty unless j < w"
    TOP = w                              # need e_0..e_{w-1}
    res = []
    for (Tc, eT, eTi, pr) in enumerate_subsets(H, q, n, rp, TOP, 1):
        lam = eT[j] if j < TOP else 0
        if lam == 0:
            continue
        ok = True
        for t in range(j + 1, w):
            if eT[t] != lam * eT[t - j] % q:
                ok = False
                break
        if ok:
            res.append({"Tidx": Tc, "lam": lam,
                        "z": (lam if (j + 1) % 2 == 0 else (-lam) % q),
                        "eT": eT})
    return res


def admissible_mine(H, q, n, k, w, c, j):
    """L3: full admissibility by MY reformulation (Q3),(Q5),(Q6),(Q8).
    Requires j < w.  Returns [{'Tidx','z','ejm1_inv','prod','eT','eTi'}]."""
    assert j < w
    A = k + w + 1
    rp = n - A
    gam = ((-1) ** rp * c) % q
    TOP = w
    BOT = j + 1
    res = []
    for (Tc, eT, eTi, pr) in enumerate_subsets(H, q, n, rp, TOP, BOT):
        lam = eT[j]
        if lam == 0:
            continue
        ok = True
        for t in range(j + 1, w):                                  # (Q3)
            if eT[t] != lam * eT[t - j] % q:
                ok = False
                break
        if not ok:
            continue
        if lam * eTi[j] % q != 1:                                  # (Q5)
            continue
        ejm1i = eTi[j - 1]
        for rho in range(0, j - 1):                                # (Q6)
            if eTi[rho] != ejm1i * eT[j - 1 - rho] % q:
                ok = False
                break
        if not ok:
            continue
        if (-pr * ejm1i * lam) % q != gam:                         # (Q8)
            continue
        res.append({"Tidx": Tc, "z": (lam if (j + 1) % 2 == 0 else (-lam) % q),
                    "ejm1_inv": ejm1i, "prod": pr, "eT": eT, "eTi": eTi})
    return res


# ------------------------------------------------------------- E_j and cosets
def Ej_from_sols(sols, mu, q, key="ejm1_inv"):
    return len(set(coset_rep(s[key], mu, q) for s in sols))


def zcosets(sols, mu, q):
    return set(coset_rep(s["z"], mu, q) for s in sols)


# ------------------------------------------------------------ structured set
def structured_sets(H, q, n, k, w, M, c):
    """{ T_MC \\ {y} } as frozensets of indices, plus the map T -> y."""
    fam = mc_family(H, q, n, k, w, M, c)
    out = {}
    for F in fam:
        Fs = set(F)
        for y in F:
            out[frozenset(Fs - {y})] = y
    return out, fam


def dist(a, b):
    """d = |a \\ b| ( = |b \\ a| for equal-size sets)."""
    return len(set(a) - set(b))


# -------------------------------------------------------------- prize rows
PRIZE_ROWS = [
    # label, n, k, w = M
    ("1/4", 2 ** 41, 2 ** 39, 2 ** 33),
    ("1/8", 2 ** 41, 2 ** 38, 2 ** 33),
    ("1/16", 2 ** 41, 2 ** 37, 2 ** 32),
]


# ------------------------------------------------------------- fixture gen
def mc3_ok(n, k, w, M):
    """MC-3 admissibility of the shape (KEY LEMMA node): M|n, M|r, w<=M, r>=M."""
    r = n - k - w
    return (n % M == 0 and r > 0 and r % M == 0 and w <= M and r >= M
            and k >= 1 and n - (k + w + 1) >= 1)
