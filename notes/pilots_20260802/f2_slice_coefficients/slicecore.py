#!/usr/bin/env python3
"""Exact b-resolved (Hamming-slice) machinery for the F2 carry-DFT model.

Pilot F2A.5 (b-resolved slice coefficients), 2026-08-02.
Builds directly on notes/pilots_20260802/f2_carry_reachability/f2model.py
(the audited first-descent model); NOTHING outside this directory is written.

------------------------------------------------------------------ model ---
Fix p odd, F_{p^2} = F_p(w), w^2 = N, psi(z) = e_p(Tr z).  A frequency
c = a_c + b_c w and the m genuine conjugate pairs of mu_n give, per pair i,
two least residues s_i^+ , s_i^- in [0, p) (f2model.residues).  An
ORIENTATION vector tau in {+1,-1}^n picks one residue per pair.  Write

    S(tau) = sum_i s_i(tau_i)   (an integer),
    h_p(r) = +1 if r mod 2p < p else -1     (the carry square wave).

The executable alignment quantity of the lane is the signed weighted sum

    A = sum_tau h_p(S(tau)) * prod_i 2 cos(pi s_i(tau_i) / p) .

(Equivalently sum_tau (-1)^{K+U} prod 2|cos| : the (-1)^U bookkeeping of
f2model is exactly the sign of the cosines, so it cancels and never has to
be carried separately.  Verified in verify_slice.py, V2.)

------------------------------------------------------------- b-resolution --
The consumer needs FIXED SIZE.  Grade by b = #{i : tau_i = +1}:

    A_b = sum_{|tau| = b} h_p(S(tau)) prod_i 2 cos(pi s_i(tau_i)/p) ,

the SLICE COEFFICIENTS.  The annealed (triangle-inequality) slice mass is

    E_b = sum_{|tau| = b} prod_i |2 cos(pi s_i(tau_i)/p)|
        = e_b(a^+ ; a^-)   (elementary symmetric, z marking the + choice),

and the object of study is the slice contraction ratio  rho_b = |A_b| / E_b.

--------------------------------------------------------- exact arithmetic --
omega = zeta_{2p} = -zeta_p^{(p+1)/2}, so EVERYTHING lives in Z[zeta_p],
represented as an integer vector of length p modulo sum_i zeta^i = 0
(canonical form: last coordinate 0).  No floats are used anywhere in the
algebra; decimal renderings are produced only by Cyc.tocomplex(), which
evaluates an exactly known algebraic number at 60 digits.

Local mode multipliers (the key simplification, exact):

    2cos(pi s/p) * omega^{k s} = omega^{(k+1)s} + omega^{(k-1)s}

so with A_i(k) = omega^{(k+1)s_i^+} + omega^{(k-1)s_i^+} and B_i(k) the
same with s_i^-,

    sum_b z^b A_b = (1/2p) sum_{k=0}^{2p-1} hhat_p(k) prod_i (z A_i(k) + B_i(k))

with hhat_p(k) = sum_r h_p(r) omega^{-k r} in Z[zeta_p] (no division needed).
Hence the per-mode slice coefficient is EXACTLY an elementary symmetric
polynomial e_b(A(k); B(k)).
"""

from __future__ import annotations

import os
import sys

sys.dont_write_bytecode = True  # never litter another pilot's directory

_HERE = os.path.dirname(os.path.abspath(__file__))
_CARRY = os.path.join(os.path.dirname(_HERE), "f2_carry_reachability")
if _CARRY not in sys.path:
    sys.path.insert(0, _CARRY)

from f2model import (  # noqa: E402
    Fp2, divisors, half_flag, is_prime, pair_reps, residues,
)

RESULTS = os.path.join(_HERE, "results")


# --------------------------------------------------------------- Z[zeta_p] --


class Cyc:
    """An element of Z[zeta_p], as an int vector of length p mod sum zeta^i.

    Canonical form has c[p-1] == 0.  Exact; never uses floating point.
    """

    __slots__ = ("p", "c")

    def __init__(self, p: int, c=None):
        self.p = p
        if c is None:
            self.c = [0] * p
        else:
            self.c = list(c)
            self._canon()

    def _canon(self):
        t = self.c[-1]
        if t:
            self.c = [x - t for x in self.c]

    @staticmethod
    def zero(p):
        return Cyc(p)

    @staticmethod
    def one(p):
        c = [0] * p
        c[0] = 1
        return Cyc(p, c)

    @staticmethod
    def zeta(p, e):
        """zeta_p^e."""
        c = [0] * p
        c[e % p] = 1
        return Cyc(p, c)

    def __add__(self, o):
        return Cyc(self.p, [a + b for a, b in zip(self.c, o.c)])

    def __sub__(self, o):
        return Cyc(self.p, [a - b for a, b in zip(self.c, o.c)])

    def __neg__(self):
        return Cyc(self.p, [-a for a in self.c])

    def __mul__(self, o):
        p = self.p
        if isinstance(o, int):
            return Cyc(p, [a * o for a in self.c])
        a, b = self.c, o.c
        out = [0] * p
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        k = i + j
                        out[k - p if k >= p else k] += ai * bj
        return Cyc(p, out)

    __rmul__ = __mul__

    def conj(self):
        p = self.p
        out = [0] * p
        for i, v in enumerate(self.c):
            out[(-i) % p] += v
        return Cyc(p, out)

    def is_zero(self):
        return not any(self.c)

    def __eq__(self, o):
        return self.p == o.p and self.c == o.c

    def __hash__(self):
        return hash((self.p, tuple(self.c)))

    def norm2(self):
        """|x|^2 as an element of the (real) ring -- exact."""
        return self * self.conj()

    def tocomplex(self, dps=60):
        """DECIMAL RENDERING of an exactly-known algebraic number (60 digits)."""
        import mpmath
        mpmath.mp.dps = dps
        p = self.p
        z = mpmath.exp(2j * mpmath.pi / p)
        return sum(v * z ** i for i, v in enumerate(self.c) if v)

    def __repr__(self):
        return f"Cyc(p={self.p}, c={self.c})"


def omega_pow(p: int, e: int) -> Cyc:
    """omega^e with omega = zeta_{2p} = -zeta_p^{(p+1)/2}.  Exact."""
    e %= 2 * p
    s = -1 if (e & 1) else 1
    z = Cyc.zeta(p, (e * ((p + 1) // 2)) % p)
    return z if s == 1 else -z


def two_cos(p: int, s: int) -> Cyc:
    """2 cos(pi s / p) = omega^s + omega^{-s}, exactly."""
    return omega_pow(p, s) + omega_pow(p, -s)


def carry_sign(p: int, r: int) -> int:
    return 1 if r % (2 * p) < p else -1


def hhat(p: int, k: int) -> Cyc:
    """hhat_p(k) = sum_{r<2p} h_p(r) omega^{-kr}  in Z[zeta_p].  Exact."""
    out = Cyc.zero(p)
    for r in range(2 * p):
        out = out + (omega_pow(p, -k * r) * carry_sign(p, r))
    return out


# ------------------------------------------------------------- instances ----


def admissible_orders(p: int) -> list[int]:
    return [n for n in divisors(p * p - 1) if n % 2 == 0 and (p - 1) % n != 0]


def instance(p: int, mu_order: int | None = None, c: tuple[int, int] | None = None,
             n: int = 8, skip: int = 0):
    """Return (F, c, locals) with locals = [(s_i^+, s_i^-)] of length n."""
    F = Fp2.make(p)
    if mu_order is None:
        mu_order = admissible_orders(p)[-1]
    mu = F.subgroup(mu_order)
    reps = pair_reps(F, mu)
    if c is None:
        c = (1, 1)
    loc = [residues(F, c, y) for y in reps[skip:skip + n]]
    return F, c, loc


def deltas_of(p: int, loc) -> list[int]:
    return [(sp - sm) % (2 * p) for sp, sm in loc]


def nus_of(p: int, loc) -> list[int]:
    """nu_i = (u_i^+ + u_i^-) mod 2, u = half_flag; the sign of the ratio."""
    return [(half_flag(p, sp) + half_flag(p, sm)) % 2 for sp, sm in loc]


def phase_index(p: int, k: int, d: int, nu: int) -> int:
    """phi_i(k) in Z/2p with arg(r_i(k)) = pi * phi_i(k) / p.  Exact index."""
    return (k * d + p * nu) % (2 * p)


# --------------------------------------------- the modified residue sigma ---
#
# h_p(r + p) = -h_p(r), so the sign (-1)^{u} of the cosine can be ABSORBED
# into the carry residue:  sigma := s + p*u  (mod 2p) makes
#
#     h_p(S(tau)) * (-1)^{U(tau)} = h_p( sum_i sigma_i(tau_i) mod 2p ) .
#
# Everything below is then governed by the ORIENTATION DIFFERENCES
#     Delta_i = sigma_i^+ - sigma_i^-  (mod 2p),
# and for every ODD mode k the phase index is exactly phi_i(k) = k Delta_i.


def sigma_of(p: int, loc):
    """[(sigma_i^+, sigma_i^-)] = [(s + p*u)] mod 2p."""
    return [((sp + p * half_flag(p, sp)) % (2 * p),
             (sm + p * half_flag(p, sm)) % (2 * p)) for sp, sm in loc]


def Delta_of(p: int, loc) -> list[int]:
    return [(a - b) % (2 * p) for a, b in sigma_of(p, loc)]


def subgroup_of(two_p: int, gens) -> int:
    """The subgroup of Z/two_p generated by gens, as a bitmask."""
    import math as _m
    g = 0
    for x in gens:
        g = _m.gcd(g, x % two_p)
    g = _m.gcd(g, two_p)
    mask = 0
    for i in range(0, two_p, g if g else two_p):
        mask |= 1 << i
    return mask


def subgroup_gen(two_p: int, gens) -> int:
    """The gcd d with <gens> = d*Z/two_p; index = d."""
    import math as _m
    g = 0
    for x in gens:
        g = _m.gcd(g, x % two_p)
    return _m.gcd(g, two_p) if g else two_p


# --------------------------------------------------- slice coefficients -----


def elem_sym(pairs) -> list[Cyc]:
    """[e_b(A;B)]_{b=0..n}, e_b = sum_{|S|=b} prod_S A prod_{S^c} B."""
    p = pairs[0][0].p
    e = [Cyc.one(p)]
    for A, B in pairs:
        new = [Cyc.zero(p) for _ in range(len(e) + 1)]
        for b, v in enumerate(e):
            new[b] = new[b] + v * B
            new[b + 1] = new[b + 1] + v * A
        e = new
    return e


def elem_sym_int(pairs) -> list[int]:
    """Integer/exact elementary symmetric for real (Cyc) magnitudes."""
    p = pairs[0][0].p
    e = [Cyc.one(p)]
    for A, B in pairs:
        new = [Cyc.zero(p) for _ in range(len(e) + 1)]
        for b, v in enumerate(e):
            new[b] = new[b] + v * B
            new[b + 1] = new[b + 1] + v * A
        e = new
    return e


def mode_pairs(p: int, k: int, loc) -> list[tuple[Cyc, Cyc]]:
    """[(A_i(k), B_i(k))] with A_i(k) = omega^{(k+1)s+} + omega^{(k-1)s+}."""
    out = []
    for sp, sm in loc:
        A = omega_pow(p, (k + 1) * sp) + omega_pow(p, (k - 1) * sp)
        B = omega_pow(p, (k + 1) * sm) + omega_pow(p, (k - 1) * sm)
        out.append((A, B))
    return out


def abs_pairs(p: int, loc) -> list[tuple[Cyc, Cyc]]:
    """[(a_i^+, a_i^-)] = [(|2cos|, |2cos|)] as exact real ring elements."""
    out = []
    for sp, sm in loc:
        ap = two_cos(p, sp)
        am = two_cos(p, sm)
        if half_flag(p, sp):
            ap = -ap
        if half_flag(p, sm):
            am = -am
        out.append((ap, am))
    return out


def slice_coeffs_bruteforce(p: int, loc) -> list[Cyc]:
    """A_b by direct enumeration of all 2^n orientations.  Exact, slow."""
    n = len(loc)
    out = [Cyc.zero(p) for _ in range(n + 1)]
    for mask in range(1 << n):
        r = 0
        b = 0
        w = Cyc.one(p)
        for i in range(n):
            if (mask >> i) & 1:
                s = loc[i][0]
                b += 1
            else:
                s = loc[i][1]
            r += s
            w = w * two_cos(p, s)
        out[b] = out[b] + w * carry_sign(p, r)
    return out


def slice_coeffs_carrydp(p: int, loc) -> list[Cyc]:
    """A_b via the graded carry transfer DP: state (b, r) in {0..n} x Z/2p."""
    two_p = 2 * p
    n = len(loc)
    dp = [[Cyc.zero(p) for _ in range(two_p)] for _ in range(n + 1)]
    dp[0][0] = Cyc.one(p)
    for i, (sp, sm) in enumerate(loc):
        wp, wm = two_cos(p, sp), two_cos(p, sm)
        nd = [[Cyc.zero(p) for _ in range(two_p)] for _ in range(n + 1)]
        for b in range(i + 1):
            row = dp[b]
            for r in range(two_p):
                v = row[r]
                if v.is_zero():
                    continue
                nd[b + 1][(r + sp) % two_p] = nd[b + 1][(r + sp) % two_p] + v * wp
                nd[b][(r + sm) % two_p] = nd[b][(r + sm) % two_p] + v * wm
        dp = nd
    out = []
    for b in range(n + 1):
        acc = Cyc.zero(p)
        for r in range(two_p):
            if not dp[b][r].is_zero():
                acc = acc + dp[b][r] * carry_sign(p, r)
        out.append(acc)
    return out


def slice_coeffs_modes(p: int, loc):
    """(twop_A_b, per_mode_e) with 2p * A_b = sum_k hhat(k) e_b(k).

    Returns the UNDIVIDED sum so that everything stays in Z[zeta_p].
    """
    n = len(loc)
    tot = [Cyc.zero(p) for _ in range(n + 1)]
    per = {}
    for k in range(2 * p):
        if k % 2 == 0:
            continue  # hhat vanishes on even modes (V4)
        H = hhat(p, k)
        e = elem_sym(mode_pairs(p, k, loc))
        per[k] = e
        for b in range(n + 1):
            tot[b] = tot[b] + H * e[b]
    return tot, per


# ---------------------------------------------------------- Krawtchouk ------


def binom_table(n: int) -> list[list[int]]:
    C = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        C[i][0] = 1
        for j in range(1, i + 1):
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
    return C


def krawtchouk_matrix(n: int) -> list[list[int]]:
    """K[b][j] = sum_{|tau|_+ = b} chi_S(tau) for any |S| = j.

    With m = n - b the number of -1 coordinates,
    K[b][j] = sum_s (-1)^s C(j,s) C(n-j, m-s)  (standard Krawtchouk K_j(m;n)).
    """
    C = binom_table(n)
    K = [[0] * (n + 1) for _ in range(n + 1)]
    for b in range(n + 1):
        m = n - b
        for j in range(n + 1):
            tot = 0
            for s in range(0, min(j, m) + 1):
                if m - s <= n - j:
                    tot += (-1) ** s * C[j][s] * C[n - j][m - s]
            K[b][j] = tot
    return K


def degree_profile_modes(p: int, loc):
    """2^n * 2p * D_j = sum_k hhat(k) e_j(A-B ; A+B).  Exact, undivided."""
    n = len(loc)
    tot = [Cyc.zero(p) for _ in range(n + 1)]
    for k in range(2 * p):
        if k % 2 == 0:
            continue
        H = hhat(p, k)
        mp_ = mode_pairs(p, k, loc)
        e = elem_sym([(A - B, A + B) for A, B in mp_])
        for j in range(n + 1):
            tot[j] = tot[j] + H * e[j]
    return tot


# --------------------------------------------- integer (unweighted) layer ---


def slice_count_dp(p: int, loc):
    """N[b][r] = #{tau : |tau| = b, S(tau) = r mod 2p}.  Pure integers."""
    two_p = 2 * p
    n = len(loc)
    dp = [[0] * two_p for _ in range(n + 1)]
    dp[0][0] = 1
    for i, (sp, sm) in enumerate(loc):
        nd = [[0] * two_p for _ in range(n + 1)]
        for b in range(i + 1):
            row = dp[b]
            for r in range(two_p):
                v = row[r]
                if v:
                    nd[b + 1][(r + sp) % two_p] += v
                    nd[b][(r + sm) % two_p] += v
        dp = nd
    return dp


def slice_reach_dp(p: int, loc):
    """R[b] = bitmask of { S(tau) mod 2p : |tau| = b }.  Pure integers."""
    two_p = 2 * p
    n = len(loc)
    full = (1 << two_p) - 1

    def rot(mask, d):
        d %= two_p
        if d == 0:
            return mask
        return ((mask << d) | (mask >> (two_p - d))) & full

    dp = [0] * (n + 1)
    dp[0] = 1
    for i, (sp, sm) in enumerate(loc):
        nd = [0] * (n + 1)
        for b in range(i + 1):
            if dp[b]:
                nd[b + 1] |= rot(dp[b], sp)
                nd[b] |= rot(dp[b], sm)
        dp = nd
    return dp
