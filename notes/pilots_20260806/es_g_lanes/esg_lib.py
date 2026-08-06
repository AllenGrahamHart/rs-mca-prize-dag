"""ES-G-LANES: exact machinery for cyclotomic-closure sizes and balance verdicts.

Self-contained.  No repo imports.  All arithmetic exact (int / Fraction) or
Decimal with an explicitly certified error pad; float is used for DISPLAY ONLY.

Objects
-------
closure_size_brute(n, W, p)   -- |closure of {1..W} under *p in Z/n|, brute force
closure_size_fast(m, W, p)    -- same for n = 2^m, ord_n(p) | 4, W < 2^(m-2)
balance(c, V_lo, V_hi, N)     -- verdict of  c*log2(V) >= N  over V in [V_lo,V_hi]
log2_binom(n, k)              -- log2 C(n,k) to certified precision
"""

from decimal import Decimal, getcontext, localcontext
from fractions import Fraction
import math

getcontext().prec = 140

# --------------------------------------------------------------------------
# 1.  cyclotomic closure sizes
# --------------------------------------------------------------------------


def mult_order(p, n):
    """multiplicative order of p mod n (n a power of two, p odd)."""
    p %= n
    assert math.gcd(p, n) == 1
    k, cur = 1, p
    while cur != 1:
        cur = (cur * p) % n
        k += 1
        assert k <= 4 * n
    return k


def closure_size_brute(n, W, p):
    """|{ p^i * s mod n : i >= 0, 1 <= s <= W }| -- brute force, small n only."""
    seen = set()
    for s in range(1, W + 1):
        x = s % n
        while x not in seen:
            seen.add(x)
            x = (x * p) % n
    return len(seen)


def _group_eps_j(m, p):
    """<p> as a list of (eps, j) with  g = eps*(1 + j*2^(m-2)) mod 2^m."""
    n = 1 << m
    half = 1 << (m - 2)
    delta = mult_order(p, n)
    assert delta in (1, 2, 4), f"ord_n(p)={delta} not in {{1,2,4}}"
    out = []
    g = 1
    for _ in range(delta):
        if g % half == 1:
            eps, h = 1, g
        else:
            assert (-g) % half == 1, "p is not +-1 mod 2^(m-2)"
            eps, h = -1, (-g) % n
        j = ((h - 1) // half) % 4
        out.append((eps, j))
        g = (g * p) % n
    assert len(set(out)) == delta
    return delta, out


def closure_size_fast(m, W, p):
    """Exact |Z| for n = 2^m, ord_n(p) in {1,2,4}, 1 <= W < 2^(m-2).

    |Z| = sum_{s=1}^{W} delta / m(s),  m(s) = #{g in <p> : g*s mod n in [1,W]}.
    m(s) depends only on (s mod 4) and on whether s >= 2^(m-2) - W.
    """
    n = 1 << m
    half = 1 << (m - 2)
    assert 1 <= W < half, "closure_size_fast requires W < 2^(m-2)"
    delta, G = _group_eps_j(m, p)

    A0 = sum(1 for (e, j) in G if e == 1)                       # r = 0 mod 4
    A2 = sum(1 for (e, j) in G if e == 1 and j % 2 == 0)        # r = 2 mod 4
    has_m3 = (-1, 3) in G                                       # r = 1 mod 4
    has_m1 = (-1, 1) in G                                       # r = 3 mod 4

    def cnt_res(r, lo, hi):
        """#{s in [lo,hi] : s = r (mod 4)}"""
        if hi < lo:
            return 0
        return (hi - r) // 4 - (lo - 1 - r) // 4

    thr = half - W                       # s >= thr enables the eps=-1 hit
    total = Fraction(0)
    total += Fraction(delta * cnt_res(0, 1, W), A0)
    total += Fraction(delta * cnt_res(2, 1, W), A2)
    for r, has in ((1, has_m3), (3, has_m1)):
        lo_hi = min(W, thr - 1)
        c_lo = cnt_res(r, 1, lo_hi)
        c_hi = cnt_res(r, max(1, thr), W)
        total += Fraction(delta * c_lo, 1)
        total += Fraction(delta * c_hi, 2 if has else 1)
    assert total.denominator == 1, f"non-integral closure size {total}"
    return int(total)


# --------------------------------------------------------------------------
# 2.  certified logarithms and balance verdicts
# --------------------------------------------------------------------------

_PAD = Decimal(10) ** -110          # certified pad on Decimal ln at prec 140


def log2_bracket(V):
    """(lo, hi) Decimals with lo <= log2(V) <= hi, V a positive int."""
    with localcontext() as ctx:
        ctx.prec = 140
        L = Decimal(V).ln() / Decimal(2).ln()
    return L - _PAD, L + _PAD


def balance(c, V_lo, V_hi, N):
    """Verdict for  c * log2(V) >= N  as V ranges over [V_lo, V_hi] (ints).

    Returns one of 'ALWAYS', 'NEVER', 'FLIPS', 'UNDECIDED' plus the two
    endpoint margins (Decimal, = c*log2 V - N).
    """
    assert c > 0 and V_lo >= 2 and V_hi >= V_lo
    lo_lo, lo_hi = log2_bracket(V_lo)
    hi_lo, hi_hi = log2_bracket(V_hi)
    Nd = Decimal(N)
    m_lo_min, m_lo_max = c * lo_lo - Nd, c * lo_hi - Nd
    m_hi_min, m_hi_max = c * hi_lo - Nd, c * hi_hi - Nd
    tol = Decimal(10) ** -40

    def sign(mn, mx):
        if mn >= 0:
            return +1
        if mx < 0:
            return -1
        if mx - mn < tol:
            return 0            # genuinely on the boundary
        return None             # precision failure

    s_lo, s_hi = sign(m_lo_min, m_lo_max), sign(m_hi_min, m_hi_max)
    if s_lo is None or s_hi is None:
        return "UNDECIDED", m_lo_min, m_hi_min
    if s_lo >= 0 and s_hi >= 0:
        v = "ALWAYS"
    elif s_lo < 0 and s_hi < 0:
        v = "NEVER"
    else:
        v = "FLIPS"
    return v, m_lo_min, m_hi_min


def log2_binom(n, k):
    """log2 C(n,k) via lgamma, Decimal-free; relative error ~1e-13 (DISPLAY/
    comparison at 1e-6 granularity only -- never used for a boundary call)."""
    if k < 0 or k > n:
        return float("-inf")
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)) / math.log(2.0)


# --------------------------------------------------------------------------
# 3.  frozen prize-row constants (sourced; see PROOFS.md for file:line)
# --------------------------------------------------------------------------

N_LOG2 = 41
N = 1 << 41                      # domain size n = 2^41
K_CROSS = 1 << 40                # rate-1/2 dimension
W_BRACKET = (1 << 34, 1 << 39)   # crossing bracket for w = a_L - k

BAND_ROWS = {                    # rate -> (k, h, d_lo, d_hi)
    "1/4":  (1 << 39, (1 << 33) + 1, (1 << 32) + 1, (1 << 33) - 1),
    "1/8":  (1 << 38, (1 << 33) + 1, (1 << 32) + 1, (1 << 33) - 1),
    "1/16": (1 << 37, (1 << 32) + 1, (1 << 31) + 1, (1 << 32) - 1),
}
BAND_BUDGET_LOG2 = math.log2(0.68) + 2 * 41       # log2(0.68 n^2)

# admissible (delta, e) classes at the maximal rate-1/2 row, and the forced
# characteristic bounds.  delta | e, e <= 6, v_2(e) <= 2, e*log2 p < 256.
#   delta = 1 : p = 1 mod 2^41          => p >= 2^41 + 1
#   delta = 2 : p = +-1 or 2^40+1 ...   => p >= 2^40 - 1
#   delta = 4 : p = +-1 mod 2^39        => p >= 2^39 - 1
DELTA_PMIN = {1: (1 << 41) + 1, 2: (1 << 40) - 1, 4: (1 << 39) - 1}
ADMISSIBLE_DE = [(d, e) for d in (1, 2, 4) for e in range(1, 7)
                 if e % d == 0 and (e & -e) <= 4]

# the seven non-identity p-classes mod 2^41 with ord | 4
def p_classes(m):
    n = 1 << m
    half = 1 << (m - 2)
    out = {}
    for eps in (1, -1):
        for j in range(4):
            g = (eps * (1 + j * half)) % n
            out[g] = mult_order(g, n)
    return out
